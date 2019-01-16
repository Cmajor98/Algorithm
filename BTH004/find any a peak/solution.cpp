#include<iostream>
#include<vector>
using namespace std;

class Solution {
	public:
		int findPeakElement(const vector<int> &num) {
			return findPeakElement(num, 0, num.size() - 1);
		}
	private:
		int findPeakElement(const vector<int> &num, int start, int end) {
			if (start == end) return start;
			if (end - start == 1) return num[start] > num[end] ? start : end;
			int mid = (end + start) / 2;
			if (num[mid] > num[mid - 1] && num[mid] > num[mid + 1]) return mid;
			else if (num[mid] < num[mid - 1])  return findPeakElement(num, start, mid - 1);
			else return findPeakElement(num, mid + 1, end);
		}
};

int main() {
	Solution s1;
	vector<int> s = { 1,2,3,1 };
	cout << s1.findPeakElement(s) << endl;
}
