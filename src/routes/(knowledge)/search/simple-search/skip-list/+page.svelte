<script>
    import Image from "$lib/Elements/Image.svelte"
    import P from "$lib/Markup/P.svelte"
    import Title from "$lib/Elements/Title.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"

    import imageSkipList from "./skip-list.svg"
    import imageSkipListInsertion from "./skip-list-insertion.svg"
    import Code from "$lib/Code/Code.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
</script>

<Title title="Список с пропусками"
/>


<P>
    Список с пропусками (skip list) &mdash; вероятностная структура данных,
    построенная на основе связного списка. Позволяет добавлять, удалять и
    искать элементы за время <Math m={`O(\\log n)`}/>.
</P>


<Image src={imageSkipList}/>

<P>
    Список с пропусками состоит из слоев. Нижний слой &mdash; обычный
    упорядоченный связный список. Каждый более высокий уровень действует
    как экспресс-полоса для списков ниже.
</P>
<P>
    Элемент появляется в слое выше с фиксированной вероятностью
    <Math m={`p`}/>. В среднем каждый элемент появляется в
    <Math m={`\\frac{1}{1-p}`}/> слоях, а общее количество слоев равно
    <Math m={`\\log_{\\frac{1}{p}} n`}/>.
</P>


<P>
    Список с пропусками состоит из узлов. У каждого узла есть значение и
    массив ссылок на следующие узлы. Ссылки распределены по уровням.
</P>
<P>
    Первому, низшему уровню соответствует индекс <Math m={`0`}/>. Длина
    массива у узла соответствует тому, на сколько элемент простирается
    вверх. Наибольшее количество ссылок у первого узла, оно же
    свидетельствует о максимальной высоте списка.
</P>


<Codeblock code={
`struct node:
    array[node*] next
    value`}
/>


<P>
    Все узлы списка с пропусками можно обернуть в один тип
    <Code c="skiplist"/>, хранящий первый узел.
</P>

<Codeblock code={
`type skiplist:
    node head

    constructor(self):
        self.head = none`}
/>


<Subheading>Поиск</Subheading>


<P>
    Нужно найти первый элемент, значение которого не меньше данного <Code c="value"/>.
</P>


<P>
    Алгоритм поиска элемента.
</P>

<EnumList wide>
    <ListItem>Начинаем поиск с первого элемента верхнего уровня.</ListItem>
    <ListItem>
        Переходим к следующему элементу, пока значение следующего элемента
        меньше искомого.
    </ListItem>
    <ListItem>
        Переместимся на уровень ниже и перейдем к шагу <Math m={`2`}/>.
    </ListItem>
</EnumList>


<Codeblock code={
`method find(skiplist self, value):
    current = self.first
    height = length of current.next

    for level = height, level >= 0, level--:
        while level < length of current.next and current.next[level].value < value:
            current = current.next[level]

    return current.next[0]`}
/>


<P>
    Во время поиска мы на каждом уровне нашли узел, который не
    превосходит <Code c="value"/>. Эту информацию можно запомнить и
    использовать в дальнейшем.
</P>

<Codeblock code={
`method find_path(skiplist self, value):
    current = self.first
    height = length of current.next
    array path[height] = [none, ..., none]

    for level = height, level >= 0, level--:
        while level < length of current.next and current.next[level].value < value:
            current = current.next[level]
        
        path[level] = current

    return path`}
/>

<Subheading>Вставка</Subheading>


<P>
    Для вставки элемента в список с пропусками нужно вставить его в
    нужное место в нижнем списке, а затем с вероятностью <Math m={`p`}/>
    проталкивать вверх, создавая новые связи. Каждый слой должен
    оставаться упорядоченным, поэтому сначала нужно найти место вставки.
</P>


<P>
    Алгоритм вставки элемента.
</P>

<EnumList wide>
    <ListItem>
        На каждом уровне найти элемент, который не превосходит вставляемое
        значение.
    </ListItem>
    <ListItem>
        Вставить элемент на последний уровень на найденную позицию.
    </ListItem>
    <ListItem>
        Пока роляет вероятность <Math m={`p`}/> проталкивать элемент вверх,
        создавая новые ссылки.
    </ListItem>
</EnumList>


<Image src={imageSkipListInsertion}/>

<Codeblock code={`
method insert(skiplist self, value):
    path = self.find_path(value)
    level = 0

    while level == 0 or random(true, false):
        if level >= length of self.head.next:
            self.head.next.append(none)
        if level >= length of path:
            path.append(self.head)
        what.next.append(none)
        path[level].next[level], what.next[level] = what, path[level].next[level]`}
/>

