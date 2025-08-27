<script>
    import Heading from "$lib/Markup/Heading.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Title from "$lib/Elements/Title.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Link from "$lib/Elements/Link.svelte"
</script>

<Title title="Графы и операции над ними"
/>

<Par>
<P>
    <b>Граф</b> &mdash; множество вершин <Math m={`V`}/> и множество рёбер <Math m={`E`}/>.
    Рёбра представляют собой неупорядоченные пары различных вершин, то есть
    <Math m={`E \\subset \\binom{V}{2} = \\{e \\in 2^V \\colon |e| = 2 \\}`}/>.
</P>
</Par>

<Par>
<P>
    Граф <Math m={`(V', E')`}/> называется <b>подграфом</b> графа <Math m={`(V, E)`}/>,
    если <Math m={`V' \\subseteq V`}/> и <Math m={`E' \\subseteq E`}/>.
</P>
<P>
    Если <Math m={`V' = V`}/>, то подграф <Math m={`(V', E')`}/> называется <b>остовным подграфом</b>
    графа <Math m={`(V, E)`}/>.
    Остовный подграф содержит все вершины исходного графа и какие-то рёбра исходного графа.
</P>
<P>
    Подграф называется <b>индуцированным подграфом</b>,
    если <Math m={`E'`}/> имеет максимально возможное количество рёбер.
    То есть индуцированный подграф графа <Math m={`(V, E)`}/> задаётся множеством вершин <Math m={`V'`}/>,
    а множество его рёбер определяется как
</P>
<Math display m={`E' = \\bigl\\{ \\{u, v\\} \\mid u \\in V' \\land u \\in V' \\land \\{u, v\\} \\in E \\bigr\\}`}/>
<P>
    Индуцированный на вершины <Math m={`V'`}/> подграф графа <Math m={`G`}/> обозначается <Math m={`G \\induced V'`}/>.
</P>
</Par>

<Par>
<P>
    У графов можно удалять вершины и рёбра.
</P>
<P>
    После удаления вершины <Math m={`v`}/> из графа <Math m={`G = (V, E)`}/> получится граф
</P>
<Math display m={`G \\without v \\defeq G \\induced (V \\without \\{ v \\})`}/>
</Par>

<Subheading>Некоторые стандартные графы</Subheading>
<Par>
<P>
    Пусть <Math m={`V = \\{1, 2, 3, \\dotsc, n-1, n\\}`}/>
</P>
<P>
    <b>Полный граф <Math m={`K_n`}/></b> &mdash; граф с <Math m={`\\binom{n}{2} = n(n-1)/2`}/> рёбрами,
    где ребра проведены между любыми двумя вершинами
</P>
<P>
    <b>Путь <Math m={`P_n`}/></b> &mdash; граф с <Math m={`n-1`}/> рёбрами;
    путь от <Math m={`1`}/> до <Math m={`n`}/>, рёбрами являются все пары
    <Math m={`\\{j, j+1\\}`}/> для <Math m={`1 \\le j < n`}/>.
</P>
<P>
    <b>Цикл <Math m={`C_n`}/></b> &mdash; граф с <Math m={`n`}/> рёбрами;
    цикл, рёбрами которого являются все пары
    <Math m={`\\{j, j \\bmod n + 1\\}`}/> для <Math m={`1 \\le j \\le n`}/>.
</P>
</Par>


<Heading>Пути и расстояния</Heading>

<Par>
<P>
    <b>Расстоянием</b> <Math m={`d(u, v)`}/> между двумя вершинами <Math m={`u`}/> и <Math m={`v`}/> &mdash;
    минимальная длина пути между вершинами <Math m={`u`}/> и <Math m={`v`}/>.
    Если пути между вершинами не существует, то <Math m={`d(u, v) = \\oo`}/>.
</P>
<P>
    Это расстояние является <Link to="/math/basics/metric-spaces">метрикой</Link>:
</P>
<Math display m={`d(v, v) = 0 \\qquad d(u, v) = d(v, u) \\qquad d(u, v) + d(v, w) \\ge d(u, w)`}/>
</Par>

<Par>
<P>
    <b>Диаметр графа</b> <Math m={`\\diam G`}/> &mdash; максимум расстояний между двумя вершинами.
</P>
<Math display m={`\\diam G = \\max_{u, v \\in V} d(u, v)`}/>
</Par>