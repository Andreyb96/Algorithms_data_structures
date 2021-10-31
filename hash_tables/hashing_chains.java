import java.util.Iterator;
import java.util.LinkedList;
import java.util.Scanner;

class Main {
    private static final int DIVIDER = 1_000_000_007;
	private static final int BASE = 263;

	public static void main(String[] args)
	{
		try (Scanner scanner = new Scanner(System.in))
		{
			HashTable hashTable = new HashTable(scanner.nextInt());
			int operationsCount = scanner.nextInt();
			for (int i = 0; i < operationsCount; i++)
			{
				String operation = scanner.next();
				if (operation.startsWith("a"))
				{
					hashTable.add(scanner.next());
				}
				else if (operation.startsWith("c"))
				{
					System.out.println(hashTable.getValues(scanner.nextInt()));
				}
				else if (operation.startsWith("f"))
				{
					System.out.println(hashTable.find(scanner.next()));
				}
				else
				{
					hashTable.delete(scanner.next());
				}
			}
		}
	}

	private static class HashTable
	{
		Words[] table;

		private HashTable(int size)
		{
			this.table = new Words[size];
		}

		private long pow(int pow)
		{
			long result = 1;
			for (int i = 0; i < pow; i++)
			{
				result = (result * BASE) % DIVIDER;
			}

			return result;
		}

		private int hashCode(String string)
		{
			long hashCode = 0;
			int i = 0;
			for (char ch : string.toCharArray())
			{
				hashCode = (((hashCode + (ch * pow(i))) % DIVIDER) + DIVIDER) % DIVIDER;
				i++;
			}

			return (int) (hashCode % table.length);
		}

		private void add(String string)
		{
			int hashCode = hashCode(string);
			if (table[hashCode] == null)
			{
				table[hashCode] = new Words();
			}
			table[hashCode].add(string);
		}

		private String find(String string)
		{
			int hashCode = hashCode(string);
			if (table[hashCode] == null || table[hashCode].isEmpty())
			{
				return "no";
			}
			else
			{
				if (table[hashCode].contains(string))
				{
					return "yes";
				}
				else
				{
					return "no";
				}
			}
		}

		private void delete(String string)
		{
			int hashCode = hashCode(string);
			if (table[hashCode] != null && !table[hashCode].isEmpty())
			{
				table[hashCode].delete(string);
			}
		}

		private String getValues(int hashCode)
		{
			if (table[hashCode] == null || table[hashCode].isEmpty())
			{
				return "";
			}
			else
			{
				return table[hashCode].getValues();
			}
		}

		private static class Words
		{
			private LinkedList<String> wordsList;

			private Words()
			{
				wordsList = new LinkedList<>();
			}

			private void add(String string)
			{
				if (!contains(string))
				{
					wordsList.addFirst(string);
				}
			}

			private boolean contains(String string)
			{
				boolean contains = false;
				for (String str : wordsList)
				{
					if (str.equals(string))
					{
						contains = true;
					}
				}
				return contains;
			}

			private void delete(String string)
			{
				Iterator<String> iterator = wordsList.iterator();
				while (iterator.hasNext())
				{
					if (iterator.next().equals(string))
					{
						iterator.remove();
						break;
					}
				}
			}

			private String getValues()
			{
				StringBuilder stringBuilder = new StringBuilder();
				for (String aWordsList : wordsList)
				{
					stringBuilder.append(aWordsList);
					stringBuilder.append(" ");
				}

				return stringBuilder.toString();
			}

			private boolean isEmpty()
			{
				return wordsList.isEmpty();
			}
		}
	}
}