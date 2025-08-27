<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import BulletList from "$lib/List/BulletList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
</script>

<Title title="Медианы"
/>

<Par>
<P>
    Мы уже много смотрели на бинарные операции в булевой алгебре.
    Настало время познакомиться с тернарной операцией, значимость которой не меньше всех бинарных.
</P>
<P>
    <b>Медиана</b> <Math m={`\\langle xyz \\rangle`}/> &mdash; тернарный булевый оператор
</P>
<Math display
      m={`\\langle x y z \\rangle = (x \\land y) \\lor (y \\land z) \\lor (z \\land x) = (x \\lor y) \\land (y \\lor z) \\land (z \\lor x)`}/>
<P>
    Эта формула выражает <b>мажоритарное значение</b> трех аргументов
</P>
<Math display m={`\\langle x y z \\rangle = y \\quad\\text{если}~ x \\le y \\le z`}/>
</Par>

<Par>
<P>
    Бинарные операции <Math m={`\\land`}/> и <Math m={`\\lor`}/> выражаются через медиану
</P>
<Math display
      m={`x \\land y = \\langle x \\, 0 \\, y\\rangle \\quad\\text{и}\\quad
          x \\lor y = \\langle x \\, 1 \\, y \\rangle`}/>
</Par>


<Heading>Алгебра медиан</Heading>

<Par>
<P>
    <b>Алгебра медиан</b> &mdash; произвольное множество <Math m={`M`}/> с определённой на ней
    тернарной операцией <Math m={`\\langle x y z \\rangle`}/>, называемой <b>медианой</b>.
    Эта операция удовлетворяет следующим свойствам
</P>
<BulletList>
    <ListItem><Math m={`\\langle x x y \\rangle = x`}/> &mdash; мажоритарность</ListItem>
    <ListItem>
        <Math m={`\\langle x y z \\rangle = \\langle x z y \\rangle = \\langle y x z \\rangle = \\langle y z x \\rangle = \\langle z x y \\rangle = \\langle z y x \\rangle`}/>
        &mdash; коммутативность
    </ListItem>
    <ListItem>
        <Math m={`\\bigl\\langle x w \\langle y w z \\rangle \\bigr\\rangle = \\bigl\\langle \\langle x w y \\rangle w z \\bigr\\rangle`}/>
        &mdash; ассоциативность
    </ListItem>
</BulletList>
<P>
    Из этих трёх аксиом следует также и дистрибутивность
</P>
<Math display
      m={`\\bigl\\langle \\langle x y z \\rangle u v \\bigr\\rangle
          = \\bigl\\langle x \\langle y u v \\rangle \\langle z u v \\rangle \\bigr\\rangle
          = \\bigl\\langle \\langle x u v \\rangle \\langle y u v \\rangle \\langle z u v \\rangle \\bigr\\rangle`}/>
</Par>

<Subheading>Идеалы</Subheading>

<Par>
<P>
    <b>Идеал</b> в алгебре медиан <Math m={`M`}/> &mdash; множество <Math m={`C \\subseteq M`}/> такое, что
</P>
<Math display m={`\\langle xyz \\rangle \\in C \\quad \\text{когда}~ x, y \\in C ~\\text{или}~ z \\in M`}/>
</Par>

<Par>
<P>
    <b>Отрезок</b> от <Math m={`u`}/> до <Math m={`v`}/> в алгебре медиан <Math m={`M`}/> &mdash; множество
</P>
<Math display m={`[u .. v] \\defeq \\bigl\\{ \\langle u x v \\rangle \\bigm| \\forall x \\in M \\bigr\\}`}/>
<P>
    Интуитивно, отрезок <Math m={`[u .. v]`}/> представляет собой множество элементов,
    &laquo;зажатых&raquo; между <Math m={`u`}/> и <Math m={`v`}/>.
    Говорят, что элемент <Math m={`x`}/> лежит в отрезке <Math m={`[u .. v]`}/>, когда <Math m={`x \\in [u .. v]`}/>,
    то есть когда <Math m={`\\langle u x v \\rangle = x`}/>.
</P>
<P>
    Любой отрезок является идеалом в алгебре медиан.
    Действительно,
    если <Math m={`\\langle u x v \\rangle \\in [u .. v]`}/> и <Math m={`\\langle u y v \\rangle \\in [u .. v]`}/>,
    то и
    <Math m={`\\bigl\\langle \\langle x u v \\rangle \\langle y u v \\rangle z \\bigr\\rangle = \\bigl\\langle \\langle x y z \\rangle u v \\bigr\\rangle \\in [u .. v]`}/>.

</P>
</Par>

<Subheading>Свойства отрезков</Subheading>

<Par>
<P>
    Отрезок с равными концами состоит только из одного элемента
</P>
<Math display m={`v \\in [u .. u] \\implies u = v \\quad\\text{или, по-другому,}\\quad [u .. u] = \\{u\\}`}/>
<P>
    На отрезки обобщается вложенность с сохранением &laquo;зажимаемости&raquo;
</P>
<Math display
      m={`x \\in [u .. v] \\land y \\in [u .. x] \\implies y \\in [u .. v] \\quad\\text{или, по-другому,}\\quad [u .. x] \\subseteq [u .. v]`}/>
</Par>


<Heading>Медианные графы</Heading>

<Par>
<P>
    Пусть <Math m={`M`}/> &mdash; алгебра медиан с операцией медианы <Math m={`\\langle \\cdots \\rangle`}/>.
    Определим граф на множестве вершин <Math m={`M`}/>, в котором рёбра проводятся по правилу
</P>
<Math display
      m={`u v \\iff
          u \\neq v ~\\text{и}~
          \\langle u x v \\rangle \\in \\{u, v\\} ~\\text{для всех}~ x \\in M`}/>
<P>
    То есть вершины <Math m={`u`}/> и <Math m={`v`}/> смежны тогда и только когда,
    когда отрезок <Math m={`[u .. v]`}/> состоит только из двух точек <Math m={`u`}/> и <Math m={`v`}/>.
</P>
</Par>

<Theorem title="Основное свойство медианного графа">
<P>
    Для любой алгебры медиан <Math m={`M`}/> построенный на ней медианный граф связный,
    при этом если какая-то вершина <Math m={`x \\in [u .. v]`}/>,
    то она лежит на кротчайшем пути между <Math m={`u`}/> и <Math m={`v`}/>.
</P>
</Theorem>