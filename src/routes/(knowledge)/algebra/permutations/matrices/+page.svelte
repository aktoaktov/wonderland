<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Code from "$lib/Code/Code.svelte"
    import Link from "$lib/Elements/Link.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import ListItem from "$lib/List/ListItem.svelte"
    import Image from "$lib/Elements/Image.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
</script>

<Title title="Матрицы перестановок"
/>

<Par>
<P>
    Перестановки можно представить в виде квадратной бинарной матрицы.
</P>
</Par>

<Par>
<P>
    <b>Матрица перестановки</b> <Math m={`\\sigma`}/> &mdash; такая матрица <Math m={`\\mat \\sigma`}/>,
    в которой на <Math m={`i`}/>-й строке цифра <Math m={`1`}/> стоит только в столбце <Math m={`\\sigma(i)`}/>,
    а остальные элементы равны <Math m={`0`}/>.
</P>
<P>
    Например,
</P>
<Math display
      m={`\\sigma = \\pmatrix{1 & 2 & 3 & 4 \\\\ 3 & 1 & 4 & 2}
          \\iff \\mat \\sigma = \\pmatrix{0 & 0 & 1 & 0 \\\\ 1 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 1 & 0 & 0}`}/>
<P>
    В матрице перестановки в каждой строке и в каждом столбце ровно одна <Math m={`1`}/>.
</P>
<P>
    У единичной перестановки матрица равна единичной матрице, <Math m={`\\mat \\1 = \\1`}/>.
</P>
</Par>

<Par>
<P>
    Матрицы перестановок можно легко использовать для выражения операций с перестановками.
    В частности,
</P>
<Math display m={`\\mat \\sigma \\cdot \\mat \\tau = \\mat (\\sigma \\compose \\tau)`}/>
<P>
    При этом <Math m={`\\mat \\sigma \\cdot (\\mat \\sigma)^\\T = (\\mat \\sigma)^\\T \\cdot \\mat \\sigma = \\1`}/>,
    поэтому матрицы перестановок ортогональны, то есть <Math m={`(\\mat \\sigma)^{-1} = (\\mat \\sigma)^\\T`}/>.
</P>
</Par>

<Par>
<P>
    Еще важное свойство: определитель матрицы перестановки равен четности этой перестановки
</P>
<Math display m={`| \\mat \\sigma | = \\sign \\sigma`}/>
</Par>

<Subheading>Матричные свойства</Subheading>

<Par>
<P>
    Следующее свойство открывает большое количество возможностей в матричных вычислениях.
    Рассмотрим пока матрицу <Math m={`P_{ij} = \\mat (ij)`}/> &mdash;
    матрицу транспозиции элементов <Math m={`i`}/> и <Math m={`j`}/>.
</P>
<P>
    При перемножении <Math m={`P_{ij}`}/> на любую матрицу <Math m={`A`}/>,
    у <Math m={`A`}/> меняются местами строки <Math m={`i`}/> и <Math m={`j`}/>.
    А если умножить <Math m={`A`}/> на <Math m={`P_{ij}`}/>,
    то в матрице <Math m={`A`}/> поменяются местами столбцы <Math m={`i`}/> и <Math m={`j`}/>.
</P>
<P>
    Мы знаем, что любую перестановку порядка <Math m={`n`}/>
    можно разложить в композицию <Math m={`n-1`}/> транспозиции.
    Значит, можно добиться любой перестановки строк и столбцов матрицы <Math m={`A`}/>
    с помощью двух матриц перестановок <Math m={`P`}/> и <Math m={`Q`}/>,
    просто посчитав <Math m={`P \\cdot A \\cdot Q`}/>.
</P>
</Par>