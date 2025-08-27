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

<Title title="Китайская теорема об остатках"
/>

<Par>
<P>
</P>
</Par>


<Theorem title="Китайская теорема об остатках">
<P>
    Пусть <Math m={`m_1, m_2, \\dotsc m_n`}/> &mdash; попарно простые натуральные числа, то есть
</P>
<Math display m={`m_i \\rprime m_j \\quad\\text{для всех}~ i \\neq j`}/>
<P>
    Система из <Math m={`n`}/> модулярных уравнений
</P>
<Math display m={`\\cases{x \\equiv r_1 \\pmod{m_1} \\\\ x \\equiv r_2 \\pmod{m_2} \\\\ \\vdots \\\\ x \\equiv r_n \\pmod{m_n} }`}/>
<P>
    имеет ровно одно решение по модулю <Math m={`m_1 m_2 \\dotsm m_n`}/>
</P>
<Math display m={`x = \\sum_{k=1}^n r_k \\cdot M_k \\cdot M_k^{-1}`}/>
<P>
    где <Math m={`M_k = \\prod_{j=1}^n m_j \\Big/ m_k`}/>, и <Math m={`M_k^{-1}`}/> &mdash; мультипликативно обратный к <Math m={`M_k \\bmod m_k`}/> в кольце <Math m={`\\ZZ_{m_k}`}/>.
</P>
</Theorem>