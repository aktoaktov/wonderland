const pseudocode = {
    comment: [
        {pattern: /(?:do something|some additional data)/g},
        {
            pattern: /(^|[^\\])#.*/,
            lookbehind: true,
            greedy: true,
        },
    ],


    string: {
        pattern: /(?:[rub]|br|rb)?("|')(?:\\.|(?!\1)[^\\\r\n])*\1/i,
        greedy: true,
    },

    "-bold-number": /\*[0-9]+\*/,

    boolean: /\b(?:false|none|true|undefined|not found|missing|empty)\b/,

    keyword:
        /\b(?:_(?=\s*:)|input|save|any|all|do|const|forever|stop|swap|type|initialize|constructor|destructor|operator|from|iterator|generator|property|record|struct|private|and|as|assert|async|await|fork|gather|join|break|case|class|continue|function|method|delete|else|except|finally|for|repeat|each|global|if|import|in|is|of|lambda|switch|not|or|pass|raise|return|try|while|with|yield)\b/,

    "soft-keyword": /\b(?:self)\b/,

    object: /\b(?:memory_allocate|memory_free|memory_copy|memory_reallocate)\b/,

    builtin:
        /\b(?:length|int|real|bool|complex|char|unsigned|object|signed|64-bit|32-bit|16-bit|8-bit)\b/,

    property: /\b(?:mutable|property)\b/,

    type: /\b(?:static_array|dynamic_array|linkedlist|skiplist|heap|beap|hash_table)\b/,



    "abstract-type":
        /\b(?:list|array|sequence|iterable|collection|set|multiset|assoc|multiassoc|dict|tuple|string|bytes)\b/,

    "class-name": [
        {
            pattern: /\b(?:node|vertex|slot)\b/g,
        },
    ],

    function: [
        {
            pattern: /((?:^|\s)(?:function|method)[ \t]+)[a-zA-Z_]\w*(?=\s*\()/g,
            lookbehind: true,
        },
        {
            pattern: /[a-zA-Z]\w*(?=\s*\()/g,
        },
    ],

    "special-boolean": {
        pattern: /⌀/u,
        alias: "boolean",
    },
    number:
        /\b0(?:b(?:_?[01])+|o(?:_?[0-7])+|x(?:_?[a-f0-9])+)\b|(?:\b\d+(?:_\d+)*(?:\.(?:\d+(?:_\d+)*)?)?|\B\.\d+(?:_\d+)*)(?:e[+-]?\d+(?:_\d+)*)?j?(?!\w)/i,
    "special-number": {
        pattern: /∞/u,
        alias: "number",
    },
    operator: /[-+@%=]=?|!=|:=|\*\*?=?|\/\/?=?|>>=|<[<=>]?|>[=>]?|[&|^~]|∈/,
    punctuation: /[{}[\];(),.:?]/,
}

export default pseudocode
