#include <iostream>
#include <string>
#include <vector>

bool isBalanced(const std::string& str, int& idx)
{
	std::string stack = "";
	std::vector<int> openedBrackets;
	auto index = 0;
	for (auto sym : str)
	{
		index++;
		if (sym == '(' || sym == '[' || sym == '{')
		{
			openedBrackets.push_back(index);
			stack.push_back(sym);
		}
		else
		{
			if (sym != ')' && sym != ']' && sym != '}')
			{
				continue;
			}
			if (stack.empty())
			{
				idx = index;
				return false;
			}
			auto top = stack[stack.size() - 1];
			if ((top == '(' && sym != ')') || (top == '[' && sym != ']') || (top == '{' && sym != '}'))
			{
				idx = index;
				return false;
			}
			stack.erase(stack.size() - 1);
			openedBrackets.pop_back();
		}
	}
	idx = openedBrackets[openedBrackets.size() - 1];
	return stack.empty();
}

int main() {
	int idx = 0;
	std::string str;
	std::cin >> str;
	if (isBalanced(str, idx))
	{
		std::cout << "Success" << std::endl;
	}
	else
	{
		std::cout << idx << std::endl;
	}
	return 0;
}