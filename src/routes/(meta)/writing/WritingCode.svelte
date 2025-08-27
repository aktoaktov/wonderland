<script>
    import Heading from "$lib/Markup/Heading.svelte"
    import Codeblock from "$lib/Code/Codeblock.svelte"
</script>

<Heading>Синтаксис псевдокода</Heading>

<Codeblock code={
`for i = 1; i <= 10; i++:
    ...`
}/>


<Codeblock code={
`forever:
    i += 1
    break if i > 10`
}/>