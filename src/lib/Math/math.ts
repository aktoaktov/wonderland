import KaTeX from "katex"
import type {KatexOptions} from 'katex'

const options: KatexOptions = {
    throwOnError: true,
    trust: true,
    strict: false,
    macros: {
        "\\xto": "\\xrightarrow{#1}",
        "\\injto": "\\hookrightarrow",
        "\\xinjto": "\\xhookrightarrow{\\,#1\\,}",
        "\\surjto": "\\twoheadrightarrow",
        "\\xsurjto": "\\xtwoheadrightarrow{\\,#1\\,}",
        "\\bijto": "\\leftrightarrow",
        "\\xbijto": "\\xleftrightarrow{\\,#1\\,}",

        "\\ptoo": "\\xrightarrow{\\mathrm{P}}",
        "\\astoo": "\\xrightarrow{\\mathrm{a.s.}\\,}",
        "\\dtoo": "\\xrightarrow{d}",

        "\\induced": "\\mid",
        "\\without": "\\setminus",
        "\\rprime": "\\perp",

        "\\sect": "\\cap",
        "\\bigsect": "\\bigcap\\limits",
        "\\union": "\\cup",
        "\\bigunion": "\\bigcup\\limits",
        "\\djunion": "\\sqcup",
        "\\bigdjunion": "\\bigsqcup\\limits",
        "\\symdiff": "\\vartriangle",

        "\\nlor": "\\mathbin{\\overline{\\lor}}",
        "\\nland": "\\mathbin{\\overline{\\land}}",
        "\\dotminus": "\\mathbin{\\mathrlap{\\mkern{4.5mu}\\raisebox{0.3em}{$\\cdot$}}{-}}",
        "\\notequiv": "\\mathbin{\\not\\equiv}",

        "\\trans": "\\operatorname{trans}", // Трансверсаль
        "\\ltrans": "\\mathop{\\overset{\\mathrm{t}}{/}}", // Левая трансверсаль
        "\\rtrans": "\\mathop{\\overset{\\mathrm{t}}{\\backslash}}", // Правая трансверсаль

        "\\biglor": "\\bigvee\\limits",
        "\\bigland": "\\bigwedge\\limits",

        "\\compose": "\\mathbin{\\footnotesize{\\boldsymbol{\\circ}}}",
        "\\bigcompose": "\\mathop{\\Large{\\boldsymbol{\\bigcirc}}}\\limits",

        "\\concat": "\\mathbin{\\leftharpoonup}",
        "\\ncirc": "\\mathbin{\\overline{\\circ}}",

        "\\const": "\\mathrm{const}",
        "\\if": "~\\mathrm{if}~",
        "\\otherwise": "~\\mathrm{otherwise}~",

        "\\stirlC": "\\genfrac{[}{]}{0pt}{}{#1}{#2}",
        "\\stirlS": "\\genfrac{\\{}{\\}}{0pt}{}{#1}{#2}",

        "\\select": "\\operatorname{select}",
        "\\rank": "\\operatorname{rank}",

        "\\uniform": "\\operatorname{uniform}",

        "\\cl": "\\operatorname{cl}",
        "\\interior": "\\operatorname{int}",
        "\\boundary": "\\partial",
        "\\diam": "\\operatorname{diam}",
        "\\mes": "\\operatorname{mes}",
        "\\vol": "\\operatorname{vol}",

        "\\ord": "\\operatorname{ord}",

        "\\im": "\\operatorname{im}",
        "\\inv": "\\operatorname{inv}",
        "\\dom": "\\operatorname{dom}",
        "\\codom": "\\operatorname{codom}",
        "\\graph": "\\operatorname{graph}",
        "\\epi": "\\operatorname{epi}",
        "\\sign": "\\operatorname{sign}",
        "\\time": "\\operatorname{time}",
        "\\space": "\\operatorname{space}",
        "\\length": "\\operatorname{length}",
        "\\bf": "\\operatorname{bf}",
        "\\height": "\\operatorname{height}",
        "\\depth": "\\operatorname{depth}",

        "\\hash": "\\operatorname{hash}",
        "\\encrypt": "\\operatorname{encrypt}",
        "\\decrypt": "\\operatorname{decrypt}",
        "\\md5": "\\operatorname{md5}",
        "\\sha256": "\\operatorname{sha256}",

        "\\hess": "\\operatorname{H}",

        "\\ave": "\\operatorname{ave}",
        "\\dev": "\\operatorname{dev}",
        "\\expect": "\\operatorname{E}",
        "\\prob": "\\operatorname{P}",
        "\\indic": "\\operatorname{I}",
        "\\var": "\\operatorname{var}",

        "\\Exp": "\\operatorname{Exp}",
        "\\Norm": "\\operatorname{N}",

        "\\mat": "\\operatorname{mat}",

        "\\GF": "\\mathrm{GF}",
        "\\GL": "\\mathrm{GL}",
        "\\SL": "\\mathrm{SL}",
        "\\SO": "\\mathrm{SO}",

        "\\LD": "\\mathrm{LD}",
        "\\KL": "\\mathrm{KL}",

        "\\Re": "\\operatorname{Re}",
        "\\Id": "\\operatorname{Id}",
        "\\Im": "\\operatorname{Im}",
        "\\Aut": "\\operatorname{Aut}",
        "\\Out": "\\operatorname{Out}",
        "\\Inn": "\\operatorname{Inn}",

        "\\eqmod": "\\stackrel{#1}{\\equiv}",
        "\\neqmod": "\\stackrel{#1}{\\notequiv}",
        "\\defeq": "\\;\\!\\stackrel{\\tiny{\\mathrm{def}}}{=}\\;\\!",
        "\\defequiv": "\\;\\!\\stackrel{\\tiny{\\mathrm{def}}}{\\equiv\\hspace*{-0.75em}\\equiv}\\;\\!",
        "\\acts": "\\mathrel{\\raisebox{0.15em}{$\\curvearrowright$}}",
        "\\notdiamond": "\\mathrel{\\not\\!\\diamond}",

        "\\isom": "\\cong",
        "\\nisom": "\\ncong",
        "\\divby": "\\mathop{\\htmlStyle{font-weight: 500;}{\\raisebox{-0.5pt}{$\\footnotesize\\vdots$}}}",
        "\\divides": "\\mid",
        "\\notdivides": "\\nmid",

        "\\oo": "\\infty",
        "\\nothing": "\\varnothing",
        "\\vphi": "\\phi",
        "\\phi": "\\varphi",
        "\\vepsilon": "\\epsilon",
        "\\epsilon": "\\varepsilon",
        "\\inf": "\\mathop{\\mathrm{inf}\\vphantom{\\mathrm{p}}}\\limits",
        "\\le": "\\leqslant",
        "\\ge": "\\geqslant",

        "\\A": "\\mathrm{A}",
        "\\B": "\\mathrm{B}",
        "\\C": "\\mathrm{C}",
        "\\D": "\\mathrm{D}",
        "\\E": "\\mathrm{E}",
        "\\F": "\\mathrm{F}",
        "\\G": "\\mathrm{G}",
        "\\H": "\\mathrm{H}",
        "\\I": "\\mathrm{I}",
        "\\J": "\\mathrm{J}",
        "\\K": "\\mathrm{K}",
        "\\L": "\\mathrm{L}",
        "\\M": "\\mathrm{M}",
        "\\N": "\\mathrm{N}",
        "\\O": "\\mathrm{O}",
        "\\P": "\\mathrm{P}",
        "\\Q": "\\mathrm{Q}",
        "\\R": "\\mathrm{R}",
        "\\S": "\\mathrm{S}",
        "\\T": "\\mathrm{T}",
        "\\U": "\\mathrm{U}",
        "\\V": "\\mathrm{V}",
        "\\W": "\\mathrm{W}",
        "\\X": "\\mathrm{X}",
        "\\Y": "\\mathrm{Y}",
        "\\Z": "\\mathrm{Z}",

        "\\NN": "\\mathbb{N}",
        "\\ZZ": "\\mathbb{Z}",
        "\\QQ": "\\mathbb{Q}",
        "\\RR": "\\mathbb{R}",
        "\\CC": "\\mathbb{C}",
        "\\HH": "\\mathbb{H}",
        "\\EE": "\\mathbb{E}",
        "\\FF": "\\mathbb{F}",

        "\\bA": "\\mathbf{A}",
        "\\bE": "\\mathbf{E}",
        "\\bL": "\\mathbf{L}",
        "\\bF": "\\mathbf{F}",
        "\\bH": "\\mathbf{H}",
        "\\bM": "\\mathbf{M}",
        "\\bS": "\\mathbf{S}",
        "\\bD": "\\mathbf{D}",

        "\\0": "\\mathbf{0}",
        "\\1": "\\mathbf{1}",

        "\\AAA": "\\mathcal{A}",
        "\\LLL": "\\mathcal{L}",
        "\\FFF": "\\mathcal{F}",
        "\\HHH": "\\mathcal{H}",
        "\\MMM": "\\mathcal{M}",
        "\\SSS": "\\mathcal{S}",
        "\\DDD": "\\mathcal{D}",
        "\\UUU": "\\mathcal{U}",

        "\\?": "\\mkern{0.4em}",

        "\\code": "\\htmlClass{code}{\\text{#1}}",

        "\\align": "\\begin{align*}#1\\end{align*}",
        "\\cases": "\\begin{cases}#1\\end{cases}",
        "\\pmatrix": "\\begin{pmatrix}#1\\end{pmatrix}",
        "\\bmatrix": "\\begin{bmatrix}#1\\end{bmatrix}",
        "\\vmatrix": "\\begin{vmatrix}#1\\end{vmatrix}",
    },
}


export const renderMath = (text: string, display = false) =>
    KaTeX.renderToString(
        text
            .replaceAll("\u000c", " ")
            .replaceAll(/\s+\\\\!\s+/g, "\\\\[0.4em]")

            .replace(/(\\\\begin\{align})(.*?)(\\\\end\{align})/g, (match, p1, p2, p3) =>
                p1 + p2.replace(/\\\\/g, '\\\\[3em]') + p3)

            .replaceAll(/_\{(.*?)=(.*?)}/g, "_{$1 \\;\\! = \\;\\! $2}") // одно =
            .replaceAll(/_\{(.*?)\s+\\le\s+(.*?)}/g, "_{$1 \\;\\! \\le \\;\\! $2}") // одно <=
            .replaceAll(/_\{(.*?)\s+\\ge\s+(.*?)}/g, "_{$1 \\;\\! \\ge \\;\\! $2}") // одно >=
            .replaceAll(/_\{(.*?)\s+\\neq\s+(.*?)}/g, "_{$1 \\;\\! \\neq \\;\\! $2}") // одно !=
            .replaceAll(/_\{(.*?)\s+\\in\s+\s(.*?)}/g, "_{$1 \\;\\! \\in \\;\\! $2}") // одно in
            .replaceAll(/_\{(.*?)\s+\\subset\s+\s(.*?)}/g, "_{$1 \\;\\! \\subset \\;\\! $2}") // одно subset
            .replaceAll(/_\{(.*?)\s+\\subseteq\s+\s(.*?)}/g, "_{$1 \\;\\! \\subseteq \\;\\! $2}") // одно subseteq
            // .replaceAll(/_\{(.*?)\\le\\s+(.*?)\\le\\s+(.*?)}/g, "_{$1 \\;\\! \\le \\;\\! $2 \\;\\! \\le \\;\\! $3}\\,")
            // .replaceAll(/_\{([^\\]*?)\\lt([^\\]*?)}/g, "_{$1 \\;\\! \\lt \\;\\! $2}")

            .replaceAll("\\forall", "\\forall\\,")
            .replaceAll("\\exists", "\\exists\\,")

            .replaceAll(/\\lim(?![a-zA-Z])/g, "\\lim\\limits")
            .replaceAll(/\\sum(?![a-zA-Z])/g, "\\sum\\limits")
            .replaceAll(/\\int(?![a-zA-Z])/g, "\\int\\limits")
            .replaceAll(/\\prod(?![a-zA-Z])/g, "\\prod\\limits")
            .replaceAll(/\\max(?![a-zA-Z])/g, "\\max\\limits")
            .replaceAll(/\\min(?![a-zA-Z])/g, "\\min\\limits")
            .replaceAll(/\\argmin(?![a-zA-Z])/g, "\\argmin\\limits")
            .replaceAll(/\\argmax(?![a-zA-Z])/g, "\\argmax\\limits")

            .replaceAll(/\\min(\s+)+\\\{/g, "\\min\\,\\{")
            .replaceAll(/\\max(\s+)+\\\{/g, "\\max\\,\\{")
        ,

        {displayMode: display, ...options},
    )