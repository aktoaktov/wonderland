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
</script>

<Title title="Кумулятивный список"
/>

<Par>
    <P>
        <b>Кумулятивный список</b> от списка <Math m={`a_1, a_2, \\dotsc, a_n`}/>
        по ассоциативной бинарной операции <Math m={`\\circ`}/> &mdash;
        список <Math m={`s_0, s_1, s_2, \\dotsc, s_n`}/>, определенный как
    </P>
    <Math display m={`s_k \\defeq \\cases{0 & \\if k = 0 \\\\ s_{k-1} \\circ a_k & \\otherwise}`}/>
    <P>
        Нерекурсивное определение
    </P>
    <Math display m={`s_k = \\bigcompose_{i=1}^k a_i = \\sum_{i=1}^k a_i`}/>
</Par>