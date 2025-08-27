<script>
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Par from "$lib/Markup/Par.svelte"
</script>

<Definition title="Математическое ожидание">
    <P>
        Пусть <Math m={`\\xi \\colon \\Omega \\to \\RR`}/> &mdash; дискретная случайная величина,
        у которой могут быть значения <Math m={`a_1, a_2, \\dotsc, a_i \\dotsc`}/>.
    </P>
    <P>
        <b>Математическим ожиданием</b> случайной величины <Math m={`\\xi`}/> называется значение
    </P>
    <Math display
          m={`\\expect \\xi = \\sum_{\\omega \\in \\Omega} \\xi(\\omega) \\cdot \\prob(\\omega) = \\sum_{i} a_i \\cdot \\prob(\\xi = a_i)`}/>

    <P>
        Аналогично, для непрерывной случайной величины <Math m={`\\xi`}/> с плотностью <Math m={`f(x)`}/>
        <b>математическое ожидание</b>
    </P>
    <Math display
          m={`\\expect \\xi = \\int_{\\Omega} \\xi(\\omega) \\cdot \\prob(d\\omega) = \\int_{-\\oo}^{\\oo} x \\cdot f(x) dx`}/>
</Definition>

<Par>
    <P>
        Важно понимать, что математическое ожидание может не существовать.
        Такое происходит, если ряд (в дискретном случае) или интеграл (в непрерывном случае) не сходятся абсолютно.
    </P>

</Par>

<Subheading>Свойства математического ожидания</Subheading>

<Par>
    <P>
        Математическое ожидание константы равно константе.
    </P>

    <Math display m={`\\expect c = c, \\text{если}~ c = \\const`}/>

    <P>
        Математическое ожидание линейно
    </P>

    <Math display m={`\\expect (a \\cdot \\xi + b \\cdot \\eta) = a \\cdot \\expect \\xi + b \\cdot \\expect \\eta`}/>
</Par>
