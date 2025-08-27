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

<Title title="Числа Стирлинга"
/>

<Heading>Числа Стирлинга второго рода</Heading>

<Par>
<P>
    <b>Число Стирлинга второго рода</b> <Math m={`\\stirlS{n}{k}`}/> &mdash; число способов разбиения множества
    из <Math m={`n`}/> элементов на <Math m={`k`}/> непустых (непересекающихся) подмножеств.
</P>
</Par>

<Par>
<P>
    Разберем некоторые частные случаи.
</P>
<P>
    <b><Math m={`k = 0`}/>.</b>
    Существует только один способ разделить пустое множество на <Math m={`0`}/> непустых частей.
    А вот непустое множество вообще не получится разделить на <Math m={`0`}/> непустых частей.
    По этому
</P>
<Math display m={`\\stirlS{n}{0} = [n = 0]`}/>
<P>
    <b><Math m={`k = 1`}/>.</b>
    Множество уже разделено на <Math m={`1`}/> часть. Значит
</P>
<Math display m={`\\stirlS{n}{1} = 1`}/>
<P>
    <b><Math m={`k = 2`}/>.</b>
    Если множество разделено на <Math m={`2`}/> непустые части, то в одной из частей должен содержаться первый элемент
    и ещё некоторое подмножество из <Math m={`n-1`}/> оставшихся элементов.
    Всего подмножеств <Math m={`2^{n-1}`}/>.
    Но подмножество не может содержать все оставшиеся элементы, потому что обе части должны быть непустыми.
    Значит
</P>
<Math display m={`\\stirlS{n}{2} = 2^{n-1} - 1`}/>
</Par>

<Par>
<P>
    Попробуем получить общую рекуррентную формулу.
    Первый элемент мы можем поместить в отдельный класс <Math m={`\\stirlS{n-1}{k-1}`}/> способами,
    либо мы можем поместить его в некоторое непустое множество из остальных <Math m={`n-1`}/> элементов.
</P>
<Math display m={`\\stirlS{n}{k} = k \\cdot \\stirlS{n-1}{k} + \\stirlS{n-1}{k-1}`}/>
</Par>