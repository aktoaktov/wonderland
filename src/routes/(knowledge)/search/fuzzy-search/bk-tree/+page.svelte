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
    import EnumList from "$lib/List/EnumList.svelte"
</script>

<Title title="Дерево Буркхарда–Келлера"
/>

<Par>
<P>
    <b>Дерево Буркхарда&ndash;Келлера</b> &mdash; метрическое дерево, поддерживающее операции
</P>
<BulletList>
    <ListItem>
        добавить строку
    </ListItem>
    <ListItem>
        найти близкие строки
    </ListItem>
</BulletList>
</Par>

<Par>
<P>
    Пусть нам нужно хранить набор <Math m={`W`}/> из <Math m={`n = |W|`}/> элементов.
</P>
<P>
    Построим дерево.
    Корень будет хранить в себе любой элемент.
    В <Math m={`k`}/>-м поддереве узла с элементом <Math m={`w`}/>
    будут храниться только такие элементы <Math m={`x`}/>, для которых <Math m={`d(w, x) = k`}/>.
</P>
</Par>