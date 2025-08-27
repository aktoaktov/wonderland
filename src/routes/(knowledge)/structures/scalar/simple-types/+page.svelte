<script>
    import Title from "$lib/Elements/Title.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Math from "$lib/Math/Math.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Code from "$lib/Code/Code.svelte"
</script>

<Title title="Простые типы"
/>

<Heading>Целые числа</Heading>

<Par>
<P>
    В идеальном мире целые числа не имеют границ.
    Наш абстрактный тип данных <Code c="int"/> представляет собой абсолютно любое целое число (элемент множества <Math m={`\\ZZ`}/>).
</P>
</Par>