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
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
</script>

<Title title="Многочлены и формальные ряды"
/>

<Par>
<P>
    <b>Многочлен</b> над переменной <Math m={`x`}/> &mdash; формальное выражение
    <Math m={`P(x) = a_0 + a_1 \\cdot x + a_2 \\cdot x^2 + \\dotsb + a_{n-1} \\cdot x^{n-1} + a_n \\cdot x^n`}/>.
</P>
<P>
    Числа <Math m={`a_j`}/> могут быть элементами любого поля. Чаще всего это <Math m={`\\RR, \\QQ, \\CC, \\GF(q)`}/>.
</P>
<P>
    Многочлены можно умножать и складывать
</P>
<Math display
      m={`\\sum_{k=0}^n a_k \\cdot x^k + \\sum_{k=0}^n b_k \\cdot x^k = \\sum_{k=0}^n (a_k + b_k) \\cdot x^k
          \\quad\\text{и}\\quad
          \\Biggl( \\sum_{k=0}^n a_k \\cdot x^k \\Biggr) \\cdot \\Biggl( \\sum_{k=0}^n b_k \\cdot x^k \\Biggr) = \\sum_{k=0}^n x^k \\sum_{i+j=k} a_i b_j`}/>
</Par>

<Par>
<P>
    <b>Степенью</b> многочлена <Math m={`A(x) = \\sum_{j=0}^n a_j \\cdot x^j`}/> называется наибольшее <Math m={`j`}/>,
    для которого <Math m={`a_j \\neq 0`}/>. Обозначается <Math m={`\\deg A`}/>.
    Почти всегда при записи многочлена в виде суммы мономов подразумевается, что <Math m={`\\deg A = n`}/>.
</P>
</Par>


<Heading>Схема Горнера</Heading>

<Par>
<P>
    Схема Горнера позволяет быстро вычислять значение многочлена, заданного коэффициентами.
</P>
</Par>