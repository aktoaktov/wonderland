<script>
    import Title from "$lib/Elements/Title.svelte"
    import Heading from "$lib/Markup/Heading.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
    import Par from "$lib/Markup/Par.svelte"
    import P from "$lib/Markup/P.svelte"
    import Subheading from "$lib/Markup/Subheading.svelte"
    import Math from "$lib/Math/Math.svelte"
</script>

<Title title="Как писать"/>

<Heading>Математические формулы</Heading>

<Subheading>Двоичное представление</Subheading>

<Par>
<P>
    Двоичное представление чисел всегда писать следующим образом
</P>
<Math display m={`j = \\bigl( \\dotsm j_2 \\, j_1 \\, j_0 \\bigr)_2`}/>
</Par>

<Codeblock code={`j = \\\\bigl( j_k \\, j_{k-1} \\\\dotsm \\\\, j_2 \\\\, j_1 \\\\, j_0 \\\\bigr)_2`}/>

<Par>
<P>
    Для Compiler Explorer использовать
</P>
</Par>
<Codeblock code="-O1 -demangle -fno-asynchronous-unwind-tables -fno-stack-protector -fverbose-asm -masm=intel -std=c++17"/>