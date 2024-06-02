# #include <iostream>
# #include <vector>
# using namespace std;

# int main() {
#     int n;
#     cin >> n;
#     vector<int> a(n);
#     for (int i = 0; i < n; i++) {
#         cin >> a[i];
#     }

#     int swaps = 0;
#     for (int i = 0; i < n; i++) {
#         while (a[i] == i + 1) { // 当前位置i的元素是i+1，需要交换
#             if (i + 1 < n) { // 保证不越界
#                 swap(a[i], a[i + 1]); // 交换相邻元素
#                 swaps++;
#             } else {
#                 // 如果是最后一个元素且仍然在正确位置，需要与前一个元素交换
#                 swap(a[i], a[i - 1]);
#                 swaps++;
#             }
#             if (i > 0) i--; // 重新检查交换后的前一个元素
#         }
#     }

#     cout << swaps << endl;
#     return 0;
# }

n = int(input())
a = list(map(int, input().split()))

cnt = i = 0
while i < n:
    while a[i] == i + 1:
        cnt += 1
        if i + 1 < n:
            a[i], a[i + 1] = a[i + 1], a[i]
        else:
            a[i], a[i - 1] = a[i - 1], a[i]
        
        if i > 0:
            i -= 1

print(cnt)