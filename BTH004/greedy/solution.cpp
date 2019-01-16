#include<iostream>
using namespace std;

class Bags
{
private:
	int capacity; //背包容量
	int value;  //背包物品总价值
	int num;  //背包编号
    int reCapacity;
public:
	Bags(int c, int n, int r, int v = 0);
	int getCapacity();
	int getValue();
	int getNum();
	int getReCapacity();
	void setValue(int v);
	void setReCapacity(int c);
};

Bags::Bags(int c, int n, int r, int v)
{
	capacity = c;
	value = v;
	reCapacity = r;
	num = n;
}

int Bags::getCapacity()
{
	return capacity;
}

int Bags::getValue()
{
	return value;
}

int Bags::getNum()
{
	return num;
}

void Bags::setValue(int v)
{
	value = v;
}

void Bags::setReCapacity(int c)
{
	reCapacity = c;
}

int Bags::getReCapacity()
{
	return reCapacity;
}


int main()
{
	//输入背包信息
	Bags *b1 = new Bags(10, 1, 10, 0);
	Bags *b2 = new Bags(10, 2, 10, 0);
	Bags *b3 = new Bags(15, 3, 15, 0);

	//输入物品信息
	int v[] = { 3,4,1,2,5,2,10 };
	int w[] = { 5,8,4,7,6,5,7 };

	double unitValue[50];
	int match[50][50] = { 0 };
	int index[50];  //物品标号
	int i;
	for (i = 0; i < 7; i++)
	{
		unitValue[i] = (double)v[i] / (double)w[i];
		index[i] = i;
	}      //计算单位价值

	for (int i = 1; i < 7; i++)    //按照单位价值排序，组成新的数组
	{
		for (int j = 0; j < 7 - i; j++)
		{
			if (unitValue[j] < unitValue[j + 1])
			{
				double b = unitValue[j];
				unitValue[j] = unitValue[j + 1];
				unitValue[j + 1] = b;

				int c = v[j];
				v[j] = v[j + 1];
				v[j + 1] = c;

				int d = w[j];
				w[j] = w[j + 1];
				w[j + 1] = d;

				int e = index[j];
				index[j] = index[j + 1];
				index[j + 1] = e;
			}
		}
	}

	//输出排序过后的物品信息
	cout << "排序过后物品价值：";
	for (int k = 0; k < 7; k++)
	{
		cout << v[k] << " ";
	}
	cout << endl;

	cout << "排序过后物品重量：";
	for (int k = 0; k < 7; k++)
	{
		cout << w[k] << " ";
	}
	cout << endl;

	cout << "物品单位价值："<<endl;
	for (int k = 0; k < 7; k++)
	{
		cout << unitValue[k]<<endl;
	}
	cout << endl;

	//输出背包信息
	cout << "背包信息：" << endl << "序号：" << b1->getNum() << " 大小：" << b1->getCapacity() << " 剩余容量：" << b1->getReCapacity() << endl;
	cout << "序号：" << b2->getNum() << " 大小：" << b2->getCapacity() << " 剩余容量：" << b2->getReCapacity() << endl;
	cout << "序号：" << b3->getNum() << " 大小：" << b3->getCapacity() << " 剩余容量：" << b3->getReCapacity() << endl;

	int x = 0;

	while (x < 7)       //贪婪（Greedy）算法的实现
	{
		if (w[x] <= b1->getReCapacity())
		{
			match[x][1] = 1;
			b1->setReCapacity(b1->getReCapacity() - w[x]);
			b1->setValue(v[x] + b1->getValue());
			x = x + 1;
			continue;
		}
		else if (w[x] <= b2->getReCapacity())
		{
			match[x][2] = 1;
			b2->setReCapacity(b2->getReCapacity() - w[x]);
			b2->setValue(v[x] + b2->getValue());
			x = x + 1;
			continue;
		}
		else if (w[x] <= b3->getReCapacity())
		{
			match[x][3] = 1;
			b3->setReCapacity(b3->getReCapacity() - w[x]);
			b3->setValue(v[x] + b3->getValue());
			x = x + 1;
			continue;
		}
		else if (w[x] > b1->getReCapacity() && w[x] > b2->getReCapacity() && w[x] > b3->getReCapacity())
		{
			x = x + 1;
			continue;
		}
	}

	//输出物品存放在背包中的信息
	cout << "背包：" << endl << "序号：" << b1->getNum() << " 大小：" << b1->getCapacity() << " 剩余容量：" << b1->getReCapacity() << " 价值：" << b1->getValue() << endl;
	cout << "序号：" << b2->getNum() << " 大小：" << b2->getCapacity() << " 剩余容量：" << b2->getReCapacity() << " 价值：" << b2->getValue() << endl;
	cout << "序号：" << b3->getNum() << " 大小：" << b3->getCapacity() << " 剩余容量：" << b3->getReCapacity() << " 价值：" << b3->getValue() << endl;

	system("pause");
	return 0;
}