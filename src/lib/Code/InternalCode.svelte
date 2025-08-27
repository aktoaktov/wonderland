<script>
    import * as grammars from "$lib/Code/grammars/index.js"
    import {highlight, tokenize} from "$lib/Code/highlighter.js"

    let {language, code} = $props()

    const grammar = grammars[language]

    console.log(code)
    console.log(grammar)

    let html = $derived.by(() => {
        if (!language) return code

        let html = highlight(tokenize(code, grammar))

        if (language === "pseudocode")
            html = html
                .replaceAll("<span class=\"operator\">^</span><span class=\"operator\">-</span><span class=\"number\">1</span>", "<sup>-1</sup>")
                .replaceAll(/<span class=\"-bold-number\">\*(.*)\*<\/span>/g, "<b><span class=\"number\">$1</span></b>")

        return html
    })


</script>

<code class={`language-${language}`}>{@html html}</code>

<style>
    code {
        print-color-adjust: exact;

        font: 0.98em/1.5em "JetBrains Mono", "Monospace", monospace;
        font-feature-settings: "cv07", "cv14", "cv16";

        white-space: pre;
        cursor: text;

        &:global(.language-pseudocode) {
            & :global(b) {
                font-weight: 800;
            }

            & :global(.comment) {
                color: #AAA
            }

            & :global(.keyword) {
                font-weight: 800;
                color: black
            }

            & :global(.abstract-type) {
                color: #39b977;
            }

            & :global(.soft-keyword) {
                color: rgb(43, 158, 203)
            }

            & :global(.special-number),
            & :global(.special-boolean) {
                font-family: 'Segoe UI';
            }
        }

        @media all {
            & :global(.keyword),
            & :global(.selector),
            & :global(.syntaxes) {
                font-weight: 600;
                color: #0734e5
            }

            & :global(.register) {
                color: #a100c5
            }

            & :global(.rule) {
                font-weight: 550;
                color: #fc2b54
            }

            & :global(.directive) {
                font-weight: 450;
                color: #08ad3d
            }

            & :global(.directive-hash) {
                color: #1cc752
            }

            & :global(.decorator) {
                color: #ff9507
            }

            & :global(.tag),
            & :global(.tag-name) {
                & :global(.punctuation) {
                    color: rgb(141, 144, 147);
                    font-weight: 450
                }
            }

            & :global(.punctuation) {
                color: #8d9093
            }

            & :global(.operator) {
                color: #636a6e;
                font-weight: 500
            }

            & :global(.builtin) {
                color: #000080
            }

            & :global(.type) {
                color: #ad0162
            }

            & :global(.object) {
                color: #0f9c8c
            }

            & :global(.class-name) {
                color: #55bef0
            }

            & :global(.constant) {
                color: rgba(154, 20, 190, 0.87)
            }

            & :global(.boolean) {
                color: #003cff;
                font-weight: 500
            }

            & :global(.number) {
                color: #5856d6
            }

            & :global(.string),
            & :global(.char),
            & :global(.attr-value) {
                color: #06c220
            }

            & :global(.function) {
                color: #3580ac
            }

            & :global(.comment) {
                color: #8e8e93
            }

            & :global(.regex) {
                color: rgb(21, 227, 121)
            }

            & :global(.property) {
                color: rgb(212, 29, 255)
            }

            & :global(.attr-name) {
                color: #1a4bd4
            }

            & :global(.http-version) {
                color: #999;
            }

            & :global(.status-code) {
                font-weight: 700;

                &:global(.status-code-info) {
                    color: #3b82f6;
                }

                &:global(.status-code-success) {
                    color: #84cc16;
                }

                &:global(.status-code-redirect) {
                    color: #eab308;
                }

                &:global(.status-code-client-error) {
                    color: #ef4444;
                }

                &:global(.status-code-server-error) {
                    color: #d946ef;
                }
            }

            & :global(.reason-phrase) {
                color: #445
            }

            & :global(.http-method) {
                font-weight: 550;
                color: white;
                border-radius: 0.25rem;
                padding: 0 0.25rem;

                min-width: 2.75rem;
                display: inline-block;
                text-align: center;

                background-color: #8e8e91;

                &:global(.http-method-get) {
                    background-color: #2fcb37
                }

                &:global(.http-method-post) {
                    background-color: #16a7ec
                }

                &:global(.http-method-delete) {
                    background-color: #f5332b
                }

                &:global(.http-method-modify) {
                    background-color: #ff9507
                }

                &:global(.http-method-connect) {
                    background-color: #5aacc2
                }

                &:global(.http-method-trace) {
                    background-color: #ab51db
                }
            }

            & :global(.pair) {
                :global(.key) {
                    color: #006ce0
                }

                :global(.value) {
                    color: #1ac522
                }
            }
        }
    }

</style>