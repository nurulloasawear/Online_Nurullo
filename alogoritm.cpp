#include <iostream>
#include <vector>
#include <queue>
#include <limits>

using namespace std;

const int INF = numeric_limits<int>::max();

// Graflarni ifodalash uchun struct
struct Edge {
    int to, weight;
};

// Eng qisqa yo‘lni topish uchun Dijkstra algoritmi
vector<int> dijkstra(int n, vector<vector<Edge>>& graph, int start) {
    vector<int> dist(n, INF);
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
    
    dist[start] = 0;
    pq.push({0, start});
    
    while (!pq.empty()) {
        int d = pq.top().first;
        int v = pq.top().second;
        pq.pop();
        
        if (d > dist[v]) continue;
        
        for (auto edge : graph[v]) {
            int to = edge.to;
            int weight = edge.weight;
            
            if (dist[v] + weight < dist[to]) {
                dist[to] = dist[v] + weight;
                pq.push({dist[to], to});
            }
        }
    }
    return dist;
}

int main() {
    int n = 5; // Tugunlar soni
    vector<vector<Edge>> graph(n);
    
    // Grafiga yo‘nalishlar qo‘shamiz
    graph[0].push_back({1, 10});
    graph[0].push_back({3, 5});
    graph[1].push_back({2, 1});
    graph[1].push_back({3, 2});
    graph[2].push_back({4, 4});
    graph[3].push_back({1, 3});
    graph[3].push_back({2, 9});
    graph[3].push_back({4, 2});
    graph[4].push_back({0, 7});
    graph[4].push_back({2, 6});
    
    int start = 0;
    vector<int> distances = dijkstra(n, graph, start);
    
    // Natijalarni chiqaramiz
    cout << "Eng qisqa yo‘llar tugundan " << start << " ga nisbatan:" << endl;
    for (int i = 0; i < n; i++) {
        cout << "Tugun " << i << ": ";
        if (distances[i] == INF) cout << "yetib bo‘lmaydi";
        else cout << distances[i];
        cout << endl;
    }
    
    return 0;
}
