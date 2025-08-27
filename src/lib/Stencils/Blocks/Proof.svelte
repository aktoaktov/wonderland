<script>
    let {children} = $props()
</script>

<div class="proof">
    {@render children?.()}
</div>

<style>
    .proof {
        padding: 0.25rem 0.75rem;
        margin: 0 -0.75rem 1.5rem;

        position: relative;

        page-break-inside: avoid;

        & :global(*):last-child {
            margin-bottom: 0;
        }

        &::before {
            content: '';
            display: block;
            position: absolute;

            left: 0;
            top: 0;

            border-radius: 10px;
            width: 3px;

            height: 100%;
            background-color: #ddd;
        }
    }
</style>