<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"

    import Image from "$lib/Elements/Image.svelte"
    import Fact from "$lib/Stencils/Blocks/Fact.svelte"
    import Definition from "$lib/Stencils/Blocks/Definition.svelte"
    import EnumList from "$lib/List/EnumList.svelte"
    import Code from "$lib/Code/Code.svelte"
</script>

<Title title="Сортировка обменами"
/>

<Par>
    <P>
        Рассмотрим методы сортировок, основными операциями в которых является обмен элементов.
        Да, эта та самая операция <Code c="swap"/>.
    </P>
</Par>

<Par>
    <P>
        Мы снова решаем задачу сортировки: нам нужно упорядочить ключи <Math m="K_1, K_2, \dotsc, K_n"/>
        по возрастанию относительного какого-то линейного порядка.
    </P>
</Par>