<script>
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Math from "$lib/Math/Math.svelte"
    import P from "$lib/Markup/P.svelte"
    import Theorem from "$lib/Stencils/Blocks/Theorem.svelte"
    import Proof from "$lib/Stencils/Blocks/Proof.svelte"
</script>

<Definition>
    <P>
        Числовой ряд <Math m={`\\sum_{n=1}^\\oo a_n`}/> называется <b>положительным</b>, если для всех <Math m="n"/>
        члены ряда <Math m="a_n \ge 0"/>.
    </P>
</Definition>

<Theorem title="Признак сравнения положительных рядов">
    <P>
        Пусть для двух рядов <Math m={`\\sum_{n=1}^\\oo a_n`}/> и <Math m={`\\sum_{n=1}^\\oo b_n`}/> выполнено
        неравенство <Math m="0 \le a_n \le b_n"/> для всех <Math m="n"/> начиная с какого-то номера. Тогда
    </P>
    <Math display m={`\\sum_{n=1}^\\oo a_n \\le \\sum_{n=1}^\\oo b_n`}/>
</Theorem>


<Theorem title="Интегральный признак сходимости">
    <P>
        Пусть <Math m="f \colon [1, +\oo) \to \RR"/> &mdash; непрерывная, неотрицательная, монотонно убывающая функция,
        <Math m="a_n = f(n)"/> при <Math m="n \in \NN"/>.
    </P>

    <P>
        Тогда несобственный интеграл <Math m={`\\int_{1}^{\\oo} f(x) dx`}/> и ряд <Math m={`\\sum_{n=1}^\\oo a_n`}/>
        сходятся или расходятся одновременно.
    </P>
</Theorem>

<Proof>
    <P>
        Функция <Math m="f"/> монотонно убывает. Значит, для <Math m="x \in [k, k+1]"/>, выполнено неравенство <Math
            m="f(k) \ge f(x) \ge f(k+1)"/>, и
    </P>
    <Math display
          m={`\\int_{k}^{k+1} f(k) dx \\ge \\int_{k}^{k+1} f(x) dx \\ge \\int_{k}^{k+1} f(k+1) dx  \\implies  f(x) \\ge \\int_{k}^{k+1} f(x) dx \\ge f(k+1)`}/>

    <P>
        Обозначим <Math m={`S_n = \\sum_{k=1}^n a_k`}/> &mdash; частичная сумма ряда <Math m={`\\sum_{n=1}^\\oo a_n`}/>.
    </P>

    <P>
        Пусть <Math m={`\\int_{1}^{\\oo} f(x) dx`}/> сходится. Тогда
    <Math m={`S_n - f(1) = f(2) + f(3) + \\dotsb + f(n) \\le \\int_1^n f(x) dx \\le \\int_1^\\oo f(x) dx`}/>
    </P>
    <P>
        Последовательность <Math m="S_n"/> частичных сумм ограничена, и при этом возрастает. Значит, ряд <Math
            m={`\\sum_{n=1}^\\oo a_n`}/> сходится.
    </P>
</Proof>