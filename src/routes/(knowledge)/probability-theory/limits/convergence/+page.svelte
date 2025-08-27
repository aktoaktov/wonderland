<script>
    import Title from "$lib/Elements/Title.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import Math from "$lib/Math/Math.svelte"
    import P from "$lib/Markup/P.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
</script>

<Title title="Сходимость"
/>

<Heading>Типы сходимости</Heading>

<Par>
    <P>
        Пусть <Math m={`\\xi_n`}/> &mdash; последовательность случайных величин,
        заданных на одном вероятностном пространстве.
    </P>
    <P>
        Для последовательностей случайных величин стандартное определение предела последовательности
        было бы слишком жестким.
        Если бы <Math m={`a = \\lim \\xi_n`}/> в стандартном определении предела последовательности,
        то для любого <Math m={`\\epsilon > 0`}/> начиная с какого-то номера все элементы
        последовательности <Math m={`\\xi_n`}/> попадали бы в отрезок <Math m={`(a - \\epsilon, a + \\epsilon)`}/>.
    </P>
</Par>


<Subheading>Сходимость по вероятности</Subheading>

<Par>
    <P>
        Давайте смотреть не факт того, что <Math m={`| \\xi_n - a | < \\epsilon`}/>, а на вероятность такого события.
    </P>
</Par>

<Definition title="Сходимость по вероятности">
    <P>
        Говорят, что последовательность <Math m={`\\xi_n`}/> <b>сходится по вероятности</b> к <Math m={`a`}/>,
        и пишут <Math m={`\\xi_n \\ptoo a`}/>, если для любого <Math m={`\\epsilon > 0`}/>
    </P>
    <Math display m={`\\lim \\prob \\big( |\\xi_n - a| < \\epsilon \\big) = 1 \\quad\\text{или}\\quad
    \\lim \\prob \\big( |\\xi_n - a| \\ge \\epsilon \\big) = 0`}/>
</Definition>


<Subheading>Сходимость почти наверное</Subheading>

<Par>
    <P>
        Попробуем сформулировать более сильное условие сходимости.
    </P>
</Par>

<Definition title="Сходимость по вероятности">
    <P>
        Говорят, что последовательность <Math m={`\\xi_n`}/> <b>сходится почти наверное</b> к <Math m={`a`}/>,
        и пишут <Math m={`\\xi_n \\astoo a`}/>, если
    </P>
    <Math display m={`\\prob \\big( \\lim \\xi_n = a \\big) = 1`}/>
</Definition>