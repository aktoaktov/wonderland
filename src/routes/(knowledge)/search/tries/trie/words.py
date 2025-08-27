class TrieNode:
    def __init__(self):
        self.children = {}  # Дочерние узлы
        self.is_end_of_word = False  # Является ли концом слова
        self.word = ""  # Само слово (если конец)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word  # Сохраняем слово

    def get_levels(self):
        levels = []
        current_level = [(self.root, 0)]  # (узел, глубина)

        while current_level:
            next_level = []
            level_data = {}  # {буква: слово} для текущего уровня

            for node, depth in current_level:
                for char, child_node in node.children.items():
                    next_level.append((child_node, depth + 1))
                    if child_node.is_end_of_word:
                        level_data[char] = child_node.word  # Сохраняем слово

            if level_data:  # Добавляем только непустые уровни
                levels.append(level_data)
            current_level = next_level

        return levels


def print_trie_table(levels, max_levels=10):
    # Собираем все уникальные буквы из всех уровней
    all_chars = sorted({char for level in levels for char in level})

    # Заголовок таблицы (уровни 1..max_levels)
    header = [" "] + [str(i + 1) for i in range(max_levels)]
    print("\t".join(header))

    # Заполняем строки для каждой буквы
    for char in all_chars:
        row = [char]
        for i in range(max_levels):
            # Проверяем, есть ли слово на этом уровне и букве
            if i < len(levels) and char in levels[i]:
                row.append(levels[i][char])
            else:
                row.append("")
        print("\t".join(row))


# Чтение слов из файла
with open('words.txt', 'r') as file:
    words = list(map(str.strip, file.readlines()))

# Построение бора и вывод таблицы
trie = Trie()
for word in words:
    trie.insert(word.upper())  # Приводим к верхнему регистру

levels = trie.get_levels()
print_trie_table(levels)