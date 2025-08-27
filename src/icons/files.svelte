<script module>
  export {file, archive, archive_opened, text_file, image_file, cloud_file}
</script>

{#snippet file(well)}
  <path d="M8 6C8 4.89543 8.89543 4 10 4H29L40 15V42C40 43.1046 39.1046 44 38 44H10C8.89543 44 8 43.1046 8 42V6Z"
        fill="#E4E5E6"/>
  <path d="M29 4L40 15H31C29.8954 15 29 14.1046 29 13V4Z" fill="#B3B6B9"/>
{/snippet}

{#snippet archive(well)}
  <rect x="8" y="4" width="32" height="40" rx="2" fill="url(#paint0_linear_24_132)"/>
  <path fill-rule="evenodd" clip-rule="evenodd"
        d="M24 4.5C24 4.22386 24.2239 4 24.5 4H25.5C25.7761 4 26 4.22386 26 4.5V5.5C26 5.77614 25.7761 6 25.5 6H24.5C24.2239 6 24 5.77614 24 5.5V4.5ZM22 6.5C22 6.22386 22.2239 6 22.5 6H23.5C23.7761 6 24 6.22386 24 6.5V7.5C24 7.77614 23.7761 8 23.5 8H22.5C22.2239 8 22 7.77614 22 7.5V6.5ZM24.5 8C24.2239 8 24 8.22386 24 8.5V9.5C24 9.77614 24.2239 10 24.5 10H25.5C25.7761 10 26 9.77614 26 9.5V8.5C26 8.22386 25.7761 8 25.5 8H24.5ZM22 10.5C22 10.2239 22.2239 10 22.5 10H23.5C23.7761 10 24 10.2239 24 10.5V11.5C24 11.7761 23.7761 12 23.5 12H22.5C22.2239 12 22 11.7761 22 11.5V10.5ZM24.5 12C24.2239 12 24 12.2239 24 12.5V13.5C24 13.7761 24.2239 14 24.5 14H25.5C25.7761 14 26 13.7761 26 13.5V12.5C26 12.2239 25.7761 12 25.5 12H24.5ZM22 14.5C22 14.2239 22.2239 14 22.5 14H23.5C23.7761 14 24 14.2239 24 14.5V15.5C24 15.7761 23.7761 16 23.5 16H22.5C22.2239 16 22 15.7761 22 15.5V14.5ZM24.5 16C24.2239 16 24 16.2239 24 16.5V17.5C24 17.7761 24.2239 18 24.5 18H25.5C25.7761 18 26 17.7761 26 17.5V16.5C26 16.2239 25.7761 16 25.5 16H24.5Z"
        fill="#E97C01"/>
  <path fill-rule="evenodd" clip-rule="evenodd"
        d="M22.8729 19C22.3728 19 21.9496 19.3694 21.8821 19.8649L20.9644 26.5947C20.7187 28.3959 22.1189 30 23.9369 30H24.0631C25.8811 30 27.2813 28.3959 27.0356 26.5947L26.1179 19.8649C26.0504 19.3694 25.6272 19 25.1271 19H22.8729ZM24 26C23.4477 26 23 26.4477 23 27C23 27.5523 23.4477 28 24 28C24.5523 28 25 27.5523 25 27C25 26.4477 24.5523 26 24 26Z"
        fill="url(#paint1_linear_24_132)"/>
  <defs>
    <linearGradient id="paint0_linear_24_132" x1="8" y1="8" x2="40" y2="40" gradientUnits="userSpaceOnUse">
      <stop stop-color="#FEDE00"/>
      <stop offset="1" stop-color="#F5C902"/>
    </linearGradient>
    <linearGradient id="paint1_linear_24_132" x1="20.9365" y1="24.4998" x2="27.0637" y2="24.4998"
                    gradientUnits="userSpaceOnUse">
      <stop stop-color="#4B4B4B"/>
      <stop offset="1" stop-color="#3B3B3B"/>
    </linearGradient>
  </defs>
{/snippet}

{#snippet archive_opened(well)}
  <rect x="8" y="4" width="32" height="40" rx="2" fill="url(#paint0_linear_24_145)"/>
  <path fill-rule="evenodd" clip-rule="evenodd"
        d="M16 4C15.4477 4 15 4.44772 15 5C15 5.55228 15.4477 6 16 6H16.6667L17 7C16.4477 7 16 7.44772 16 8C16 8.55228 16.4477 9 17 9H17.6667L18 10C17.4477 10 17 10.4477 17 11C17 11.5523 17.4477 12 18 12H18.6667L19 13C18.4477 13 18 13.4477 18 14C18 14.5523 18.4477 15 19 15H19.6667L20 16C19.4477 16 19 16.4477 19 17C19 17.5523 19.4477 18 20 18H20.6667L21 19C20.4477 19 20 19.4477 20 20C20 20.5523 20.4477 21 21 21H21.6667L23 25H25L26.3333 21H27C27.5523 21 28 20.5523 28 20C28 19.4477 27.5523 19 27 19L27.3333 18H28C28.5523 18 29 17.5523 29 17C29 16.4477 28.5523 16 28 16L28.3333 15H29C29.5523 15 30 14.5523 30 14C30 13.4477 29.5523 13 29 13L29.3333 12H30C30.5523 12 31 11.5523 31 11C31 10.4477 30.5523 10 30 10L30.3333 9H31C31.5523 9 32 8.55228 32 8C32 7.44772 31.5523 7 31 7L31.3333 6H32C32.5523 6 33 5.55228 33 5C33 4.44772 32.5523 4 32 4H31H17H16Z"
        fill="#E97C01"/>
  <path fill-rule="evenodd" clip-rule="evenodd"
        d="M22.9366 23C22.4365 23 22.0133 23.3694 21.9457 23.8649L21.028 30.5947C20.7824 32.3959 22.1826 34 24.0005 34H24.1268C25.9448 34 27.3449 32.3959 27.0993 30.5947L26.1816 23.8649C26.114 23.3694 25.6908 23 25.1908 23H22.9366ZM24.0637 30C23.5114 30 23.0637 30.4477 23.0637 31C23.0637 31.5523 23.5114 32 24.0637 32C24.6159 32 25.0637 31.5523 25.0637 31C25.0637 30.4477 24.6159 30 24.0637 30Z"
        fill="url(#paint1_linear_24_145)"/>
  <defs>
    <linearGradient id="paint0_linear_24_145" x1="8" y1="8" x2="40" y2="40" gradientUnits="userSpaceOnUse">
      <stop stop-color="#FEDE00"/>
      <stop offset="1" stop-color="#F5C902"/>
    </linearGradient>
    <linearGradient id="paint1_linear_24_145" x1="21.0002" y1="28.4998" x2="27.1273" y2="28.4998"
                    gradientUnits="userSpaceOnUse">
      <stop stop-color="#4B4B4B"/>
      <stop offset="1" stop-color="#3B3B3B"/>
    </linearGradient>
  </defs>
{/snippet}

{#snippet text_file(well)}
  <path d="M8 6C8 4.89543 8.89543 4 10 4H29L40 15V42C40 43.1046 39.1046 44 38 44H10C8.89543 44 8 43.1046 8 42V6Z"
        fill="#E4E5E6"/>
  <path d="M29 4L40 15H31C29.8954 15 29 14.1046 29 13V4Z" fill="#B3B6B9"/>
  <rect x="13" y="20" width="14" height="2" rx="0.5" fill="#828384"/>
  <rect x="13" y="25" width="22" height="2" rx="0.5" fill="#828384"/>
  <rect x="13" y="35" width="20" height="2" rx="0.5" fill="#828384"/>
  <rect x="13" y="30" width="17" height="2" rx="0.5" fill="#828384"/>
{/snippet}


{#snippet image_file(well)}
  <path d="M8 6C8 4.89543 8.89543 4 10 4H29L40 15V42C40 43.1046 39.1046 44 38 44H10C8.89543 44 8 43.1046 8 42V6Z"
        fill="#B3D9FF"/>
  <path d="M29 4L40 15H31C29.8954 15 29 14.1046 29 13V4Z" fill="#4595E6"/>
  <path
      d="M26.9761 28.7928C27.7748 27.8532 29.2252 27.8532 30.0239 28.7928L35.5995 35.3524C36.1516 36.0018 35.69 37 34.8376 37H22.1624C21.31 37 20.8484 36.0018 21.4005 35.3524L26.9761 28.7928Z"
      fill="#436DCD"/>
  <path
      d="M19.8615 24.3407C20.6577 23.2032 22.3423 23.2032 23.1385 24.3407L30.8986 35.4265C31.3625 36.0893 30.8884 37 30.0793 37H12.9207C12.1116 37 11.6375 36.0893 12.1014 35.4265L19.8615 24.3407Z"
      fill="#153F7B"/>
  <g filter="url(#filter0_d_26_217)">
    <circle cx="30" cy="22" r="2" fill="#FEFFD0"/>
  </g>
  <defs>
    <filter id="filter0_d_26_217" x="26" y="18" width="8" height="8" filterUnits="userSpaceOnUse"
            color-interpolation-filters="sRGB">
      <feFlood flood-opacity="0" result="BackgroundImageFix"/>
      <feColorMatrix in="SourceAlpha" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 127 0"
                     result="hardAlpha"/>
      <feOffset/>
      <feGaussianBlur stdDeviation="1"/>
      <feComposite in2="hardAlpha" operator="out"/>
      <feColorMatrix type="matrix" values="0 0 0 0 1 0 0 0 0 0.981667 0 0 0 0 0.541667 0 0 0 0.25 0"/>
      <feBlend mode="normal" in2="BackgroundImageFix" result="effect1_dropShadow_26_217"/>
      <feBlend mode="normal" in="SourceGraphic" in2="effect1_dropShadow_26_217" result="shape"/>
    </filter>
  </defs>
{/snippet}

{#snippet cloud_file(well)}
  <path d="M8 6C8 4.89543 8.89543 4 10 4H29L40 15V42C40 43.1046 39.1046 44 38 44H10C8.89543 44 8 43.1046 8 42V6Z"
        fill="#B3F2FF"/>
  <path d="M29 4L40 15H31C29.8954 15 29 14.1046 29 13V4Z" fill="#45CBE6"/>
  <path fill-rule="evenodd" clip-rule="evenodd"
        d="M13 29C13 31.7614 15.2386 34 18 34H31C33.2091 34 35 32.2091 35 30C35 27.7909 33.2091 26 31 26C30.6327 26 30.277 26.0495 29.9391 26.1422C29.5229 23.2348 27.0225 21 24 21C21.755 21 19.7979 22.233 18.7691 24.0588C18.5184 24.0201 18.2616 24 18 24C15.2386 24 13 26.2386 13 29Z"
        fill="url(#paint0_linear_25_206)" fill-opacity="0.9"/>
  <defs>
    <linearGradient id="paint0_linear_25_206" x1="17.5" y1="21" x2="30.5" y2="34" gradientUnits="userSpaceOnUse">
      <stop stop-color="#2AA4F4"/>
      <stop offset="1" stop-color="#007AD9"/>
    </linearGradient>
  </defs>
{/snippet}