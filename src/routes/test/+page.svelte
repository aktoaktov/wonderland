<script>
    import Tooltip from "$lib/Elements/Tooltip.svelte"
    import P from "$lib/Markup/P.svelte"
</script>

<P>
    Здесь большой и длинный текст, где есть
    <Tooltip inline>
        {#snippet content()}Здесь какое-то содержимое тултипа{/snippet}
        объект, очень-очень длинный объект, такой, что не помещается на одной строчке и ему приходится вылазить
    </Tooltip>, который что-то делает
</P>
