<script lang="ts">
    import * as icons from "icons"

    interface Icon {
        name: string,
        size: number,
        margin?: number,
        color?: string,
        well?: boolean,
    }

    let {
        name, well = false,
        size = 1.5, margin = 0, color = undefined,
    }: Icon = $props()
</script>

<style>
    svg {
        vertical-align: middle;
    }
</style>

<svg style:height="{size}rem" style:margin="{margin}rem" style:color={color && `var(--${color})`}
     viewBox="0 0 48 48" fill="currentColor"
     xmlns="http://www.w3.org/2000/svg">
    {@render icons[name.replaceAll('-', '_')]?.(well)}
</svg>