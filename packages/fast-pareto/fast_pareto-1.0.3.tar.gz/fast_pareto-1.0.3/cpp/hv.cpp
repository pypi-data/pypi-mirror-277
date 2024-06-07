#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>

using std::vector;


std::pair<vector<vector<double>>, vector<int>> _unique_and_inverse(const vector<vector<double>> costs){
    int n_trials = costs.size();
    int n_objectives = costs[0].size();
    vector<vector<double>> sorted_costs_and_index = costs;
    for (int n = 0; n < n_trials; ++n) {
        sorted_costs_and_index[n].push_back((double) n);
    }
    sort(sorted_costs_and_index.begin(), sorted_costs_and_index.end());
    vector<vector<double>> unique_lexsorted_costs;
    auto push_back_cost = [&](int index) -> void{
        int original_index = (int) sorted_costs_and_index[index][n_objectives];
        unique_lexsorted_costs.push_back(costs[original_index]);
    };
    vector<int> order_inv(n_trials);
    int rank = 0;
    order_inv[(int) sorted_costs_and_index[0][n_objectives]] = rank;
    push_back_cost(0);
    for (int n = 1; n < n_trials; ++n) {
        int prev = (int) sorted_costs_and_index[n - 1][n_objectives];
        int cur = (int) sorted_costs_and_index[n][n_objectives];
        bool is_duplicated = std::equal(costs[cur].begin(), costs[cur].end(), costs[prev].begin());
        if (!is_duplicated) {
            push_back_cost(n);
        }
        order_inv[cur] = is_duplicated ? rank : ++rank;
    }
    return std::make_pair(unique_lexsorted_costs, order_inv);
}

template <class T>
vector<T> _filter(const vector<T>& vec, const vector<bool>& mask){
    vector<T> new_vec;
    for (int i = 0; i < (int) vec.size(); ++i){
        if (mask[i]){
            new_vec.push_back(vec[i]);
        }
    }
    return new_vec;
}

int _argmax(const vector<double>& vec){
    double max_value = *std::max_element(vec.begin(), vec.end());
    for (int i = 0; i < (int) vec.size(); ++i){
        if (max_value == vec[i]) {
            return i;
        }
    }
    return -1;
}

vector<double> _elementwise_max(const vector<double>& vec1, const vector<double>& vec2){
    vector<double> new_vec(vec1.size());
    for (int i = 0; i < (int) vec1.size(); ++i){
        new_vec[i] = std::max(vec1[i], vec2[i]);
    }
    return new_vec;
}

vector<bool> _is_pareto_front(vector<vector<double>> unique_lexsorted_costs) {
    int n_trials = unique_lexsorted_costs.size();
    int n_objectives = unique_lexsorted_costs[0].size();
    vector<bool> on_front = vector<bool>(n_trials, false);
    vector<int> nondominated_indices(n_trials);
    for (int n = 0; n < n_trials; ++n){
        nondominated_indices[n] = n;
    }
    while (unique_lexsorted_costs.size() > 0) {
        auto& cost = unique_lexsorted_costs[0];
        int n_kept = unique_lexsorted_costs.size();
        vector<bool> nondominated_and_not_top(n_kept, false);
        for (int n = 1; n < n_kept; ++n) {
            for (int m = 0; m < n_objectives; ++m) {
                if (unique_lexsorted_costs[n][m] < cost[m]) {
                    nondominated_and_not_top[n] = true;
                    break;
                }
            }
        }
        on_front[nondominated_indices[0]] = true;
        vector<int> new_nondominated_indices = _filter(nondominated_indices, nondominated_and_not_top);
        vector<vector<double>> new_costs = _filter(unique_lexsorted_costs, nondominated_and_not_top);
        swap(nondominated_indices, new_nondominated_indices);
        swap(unique_lexsorted_costs, new_costs);
    }
    return on_front;
}

vector<bool> is_pareto_front(const vector<vector<double>>& costs, bool assume_unique_lexsorted){
    if (!assume_unique_lexsorted) {
        vector<vector<double>> unique_lexsorted_costs;
        vector<int> order_inv;
        std::tie(unique_lexsorted_costs, order_inv) = _unique_and_inverse(costs);
        vector<bool> on_front = _is_pareto_front(unique_lexsorted_costs);
        int n_trials = costs.size();
        vector<bool> on_front_original = vector<bool>(n_trials);
        for (int n = 0; n < n_trials; ++n) {
            on_front_original[n] = on_front[order_inv[n]];
        }
        return on_front_original;
    }
    return _is_pareto_front(costs);
}

double _compute_inclusive_hv(const vector<double>& cost, const vector<double>& reference_point){
    double inclusive_hv = 1.0;
    for (int m = 0; m < (int) reference_point.size(); ++m) {
        inclusive_hv *= reference_point[m] - cost[m];
    }
    return inclusive_hv;
}

double _compute_hypervolume(const vector<vector<double>>& sorted_costs, const vector<double>& reference_point){
    int n_trials = sorted_costs.size();
    vector<double> inclusive_hvs = vector<double>(n_trials);
    for (int n = 0; n < n_trials; ++n) {
        inclusive_hvs[n] = _compute_inclusive_hv(sorted_costs[n], reference_point);
    }
    if (n_trials == 1) {
        return inclusive_hvs[0];
    } else if (n_trials == 2) {
        vector<double> intersec_node = _elementwise_max(sorted_costs[0], sorted_costs[1]);
        double intersec = _compute_inclusive_hv(intersec_node, reference_point);
        return inclusive_hvs[0] + inclusive_hvs[1] - intersec;
    }

    double hv = 0.0;
    auto _compute_exclusive_hv = [](const vector<vector<double>>& limited_costs, const vector<double>& reference_point, double inclusive_hv) -> double {
        if (limited_costs.size() == 0) {
            return inclusive_hv;
        }
        vector<bool> on_front = is_pareto_front(limited_costs, false);
        vector<vector<double>> pareto_limited_costs = _filter(limited_costs, on_front);
        return inclusive_hv - _compute_hypervolume(pareto_limited_costs, reference_point);
    };
    for (int n = 0; n < n_trials; ++n) {
        vector<vector<double>> limited_costs;
        auto& cost = sorted_costs[n];
        for (int i = n + 1; i < n_trials; ++i) {
            vector<double> limited_cost = _elementwise_max(cost, sorted_costs[i]);
            limited_costs.push_back(limited_cost);
        }
        hv += _compute_exclusive_hv(limited_costs, reference_point, inclusive_hvs[n]);
    }
    return hv;
}

double compute_hypervolume(const vector<vector<double>>& costs, const vector<double>& ref_point){
    vector<bool> on_front = is_pareto_front(costs, false);
    vector<vector<double>> pareto_costs = _filter(costs, on_front);
    sort(pareto_costs.begin(), pareto_costs.end());
    return _compute_hypervolume(pareto_costs, ref_point);
}
