<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Statement from "$lib/Stencils/Blocks/Statement.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Math from "$lib/Math/Math.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
</script>

<Title title="Система непересекающихся множеств"
/>


<P>
    Система непересекающихся множеств &mdash; структура данных, позволяющая объединять непересекающиеся множества и
    отвечать на разные запросы про них.
</P>

<P>
    Изначально у нас есть <Math m="n"/> элементов, каждый из которых находится в своем независимом множестве.
    Структура поддерживает несколько основных операций
</P>

<BulletList>
    <ListItem>
        <Code c="unite(set a, set b)"/> &mdash; объединение двух множеств в одно
    </ListItem>
    <ListItem>
        <Code c="get(object x)"/> &mdash; получение множества, в котором находится данный элемент
    </ListItem>
    <ListItem>
        <Code c="size(set s)"/> &mdash; получение количества элементов в множестве
    </ListItem>
</BulletList>

<Heading>Устройство структуры</Heading>

<P>
    Множества хранятся в&nbsp;виде корневых деревьев, а&nbsp;сами элементы множеств хранятся в&nbsp;вершинах.
    В&nbsp;корне дерева хранится представитель этого множества (лидер).
    В&nbsp;каждой вершине хранится ссылка на родителя.
    Если у какого-то элемента ссылка на&nbsp;родителя указывает&nbsp;на&nbsp;него&nbsp;же, то&nbsp;этот элемент является
    лидером.
    Операция получения множества, в&nbsp;котором хранится данный элемент, будет возвращать нам лидера этого множества.
    При&nbsp;объединении двух множеств деревья объединяются: корень одного дерева подвешивается к&nbsp;корню другого.
</P>

<P>
    Пусть, для простоты, элементы множеств пронумерованы от <Math m="0"/> до <Math m="n-1"/>.
    Родителей элементов можно хранить в массиве <Code c="parents"/>, тогда родитель элемента <Code c="x"/> &mdash;
    элемент
    <Code c="parent[x]"/>.
</P>

<P>
    При инициализации структуры каждый элемент должен попасть в свое собственное независимое множество
</P>

<Codeblock code={
`array[int] parents[n]

for i = 0, i < n:
    parents[i] = i`
}/>


<Heading>Наивная реализация</Heading>

<P>
    Каждое множество в структуре связано со своим лидером.
    Операция <Code c="get"/> будет возвращать лидера множества, в котором содержится элемент <Code c="x"/>.
</P>

<P>
    Для выполнения операции нужно просто пройтись вверх по дереву, пока не дойдем до лидера.
</P>

<Codeblock code={
`function get(int x) -> int:
    if parent[x] == x:
        return x
    else:
        return get(parent[x])`
}/>

<P>
    Для объединения двух множеств достаточно подвесить одно дерево к другому. Для этого найдем корни каждого дерева
    (лидеры каждого множества) и перезапишем ссылку на родителя одного из них.
</P>

<Codeblock code={
`function unite(int a, int b):
    a = get(a)
    b = get(b)
    parent[a] = b`
}/>

<P>
    При такой реализации обе операции занимают время <Math m="O(n)"/>, потому что дерево может оказаться бамбуком.
</P>

<Heading>Эвристика сжатия пути</Heading>

<P>
    Давайте ускорим операцию <Code c="get"/>. После того, как мы нашли лидера множества, в котором находится элемент
    <Math m="x"/> мы можем подвесить <Code c="x"/> к этому лидеру. Тогда последующие выполнения операции <Code
        c="get(x)"/> будут работать за время <Math m="O(1)"/> (естественно, при условии, что это множество ни с кем не
    объединяется).
</P>

<Codeblock code={
`function get(int x) -> int:
    if parent[x] == x:
        return x
    else:
        parent[x] = get(parent[x])
        return parent[x]`
}/>

<P>
    Этот прием называется <b>эвристикой сжатия пути</b>. Действительно, мы &laquo;сжимаем&raquo; путь до корня,
    подвешивая все его вершины к корню.
</P>