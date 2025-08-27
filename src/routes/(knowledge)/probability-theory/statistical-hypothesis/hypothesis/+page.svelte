<script>
    import Title from "$lib/Elements/Title.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Par from "$lib/Markup/Par.svelte"
</script>

<Title title="Статистические гипотезы"
/>

<Definition title="Статистическая гипотеза">
    <P>
        Пусть в эксперименте мы наблюдаем случайную величину <Math m={`\\xi`}/>, распределение которой полностью или частично неизвестно.
    </P>
    <P>
        Любое утверждение про это распределение называется <b>статистической гипотезой</b>.
    </P>
</Definition>


<Par>
    <P>
        Например, пусть у нас есть независимая выборка
        <Math m={`\\xi_1, \\xi_2, \\dotsc, \\xi_n \\sim \\Norm(\\mu, 1)`}/>.
        В этом распределении нам неизвестен параметр <Math m={`\\mu`}/>, и мы хотим его оценить.
    </P>
    <P>
        Тогда можно выдвинуть статистическую гипотезу <Math m={`H = (\\mu = 2)`}/>.
    </P>
</Par>