<script>
    import Title from "$lib/Elements/Title.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import P from "$lib/Markup/P.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
</script>

<Title title="Числовые последовательности"
/>

<Definition title="Последовательность">
    <P>
        <b>Числовая последовательность</b> <Math m="x_n"/> &mdash; функция <Math m="x \colon \NN \to \RR"/>,
        при которой <Math m="n \mapsto x_n"/>.
    </P>
</Definition>

<Heading>Предел</Heading>

<Definition title="Предел последовательности">
    <P>
        Число <Math m="a"/> называется <b>пределом</b> числовой последовательности <Math m="x_n"/>, если
    </P>

    <Math display
          m={`\\forall \\epsilon > 0 \\enspace \\exists N \\in \\NN \\colon\\: \\forall n > N \\quad |x_n - a| < \\epsilon`}/>

    По-другому, в любую окрестность <Math m="a"/> будут попадать все члены последовательности,
    начиная с какого-то номера.
</Definition>

<P>
    Предел последовательности <Math m="x_n"/> обозначается <Math m="\lim x_n"/> или, более развернуто, <Math
        m={`\\lim_{n \\to \\infty} x_n`}/>.
</P>

<P>
    Например, у последовательности <Math m={`x_n = \\frac{1}{n}`}/>
    предел <Math m={`\\lim_{n \\to \\infty} \\frac{1}{n} = 0`}/>, так как для любого <Math m="\\epsilon"/> можно
    явно указать номер <Math m={`N = \\lceil \\frac{1}{\\epsilon} \\rceil`}/>, начиная с которого все члены
    последовательности <Math m="x_n"/> при <Math m="n > N"/> будут меньше <Math m="\epsilon"/>.
</P>

<P>
    Предела у последовательности может и не быть. Например, у <Math m="x_n = (-1)^n"/>.
</P>

<P>
    Если у последовательности есть предел, то говорят, что последовательность сходится.
</P>


<Definition title="Подпоследовательность">
    <P>Пусть <Math m="x_n"/> &mdash; какая-то последовательность.</P>
    <P>
        Выберем натуральные числа <Math m="n_1 < n_2 < n_3 < \dotsb < n_k < \dotsb"/> и построим новую
        последовательность <Math m={`y_k \\equiv x_{n_k}`}/>.
    </P>
    <P>
        Эта последовательность называется <b>подпоследовательностью</b> последовательности <Math m="x_n"/>.
    </P>
</Definition>

<Theorem title="Теорема о сходимости подпоследовательности">
    <P>
        Пусть <Math m="x_n"/> &mdash; сходящаяся последовательность и <Math m="y_n"/> &mdash; любая
        подпоследовательность <Math m="x_n"/>. Тогда
    </P>
    <Math display m="\lim x_n = \lim y_n"/>
</Theorem>

<Proof>
    <P>
        Пусть <Math m={`y_k = x_{n_k}`}/> (<Math m="n_k"/> &mdash; номер элемента <Math m="k"/>
        последовательности <Math m="y_k"/> в последовательности <Math m="x_n"/>). Понятно, что <Math m="n_k \ge k"/>.
    </P>

    <P>
        Пусть <Math m="N"/> &mdash; такое число, что <Math m="\forall n > N \enspace \big| x_n - \lim x_n \big| < \epsilon"/>.
        Для любых <Math m="k > N"/> выполняется неравенство <Math m="n_k > N"/>. Тогда <Math m={`\\forall k > N \\enspace \\big| y_k - \\lim x_n \\big| = \\big| x_{n_k} - \\lim x_n \\big| < \\epsilon`}/>.
    </P>

    <P>
        Получили, что <Math m="\lim y_k = a = \lim x_n"/>.
    </P>

</Proof>