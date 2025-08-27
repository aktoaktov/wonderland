<script>
    import Title from "$lib/Elements/Title.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import Math from "$lib/Math/Math.svelte"
    import P from "$lib/Markup/P.svelte"
    import Par from "$lib/Markup/Par.svelte"
</script>

<Title title="Кодирование"
/>

<Definition title="Кодирование">
    <P>
        Пусть есть два языка <Math m={`L`}/> и <Math m={`M`}/>.
    </P>
    <P>
        <b>Кодирование</b> &mdash; инъективное отображение
    </P>
    <Math display m={`c \\colon L \\injto M`}/>
</Definition>

<Par>
    <P>
        Другими, более филосовскими словами, кодирование &mdash; преобразование информации между разными системами
        представления, в качестве которых мы рассматриваем языки.
    </P>
</Par>