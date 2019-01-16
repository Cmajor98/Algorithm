#include <iostream>
using namespace std;

class solution {
public:
	solution(int cpNum) : cpNum(cpNum) {
		free_m = new bool[cpNum];
		free_w = new bool[cpNum];
		result = new int[cpNum];
		order_m = new int*[cpNum];
		order_w = new int*[cpNum];
		for (int i = 0; i < cpNum; ++i) {
			order_m[i] = new int[cpNum];
			order_w[i] = new int[cpNum];
		}
	}
	~solution() {
		for (int i = 0; i < cpNum; ++i) {
			delete[] order_m[i];
			delete[] order_w[i];
		}
		delete[] free_m;
		delete[] free_w;
		delete[] result;
		delete[] order_m;
		delete[] order_w;
	}
	// 输入男性和女性的排序表
	void init() {
		cout << "[man's order list of women]\n";
		for (int i = 0; i < cpNum; ++i) {
			cout << "[m-" << i << "]: ";
			for (int j = 0; j < cpNum; ++j) {
				cin >> order_m[i][j];
			}
			free_m[i] = true;
		}
		cout << "[woman's order list of man]\n";
		for (int i = 0; i < cpNum; ++i) {
			cout << "[w-" << i << "]: ";
			int man;
			for (int j = 0; j < cpNum; ++j) {
				cin >> man;
				order_w[i][man] = cpNum - j;
			}
			free_w[i] = true;
			result[i] = -1;
		}
	}
	// 判断是否全部人都脱单
	bool isOk() const {
		for (int i = 0; i < cpNum; ++i)
			if (free_m[i]) return false;
		return true;
	}
	void solve() {
		while (true) {
			for (int i = 0; i < cpNum; ++i) {
				if (free_m[i]) {
					for (int j = 0; j < cpNum && free_m[i]; ++j) {
						int w = order_m[i][j];
						// 女方目前自由
						if (free_w[w]) {
							result[w] = i;
							free_m[i] = false;
							free_w[w] = false;
						}
						// 女方已有对象，但爱此男比爱现任多一点
						else {
							if (order_w[w][i] > order_w[w][result[w]]) {
								free_m[result[w]] = true;
								result[w] = i;
								free_m[i] = false;
							}
						}
					}
				}
			}
			if (isOk()) break;
		}
	}
	// 输出匹配结果
	void print() const {
		for (int i = 0; i < cpNum; ++i) {
			cout << "(w-" << i << ", m-" << result[i] << ")\n";
		}
	}
private:
	bool* free_m;
	bool* free_w;
	int** order_m;
	int** order_w;
	int*  result;
	int   cpNum;
};

int main() {
	cout << "Please input the number of couples: " << endl;
	int cpNum;
	cin >> cpNum;
	solution sl(cpNum);
	sl.init();
	sl.solve();
	sl.print();
	return 0;
}