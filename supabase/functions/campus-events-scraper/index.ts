// Follow this setup guide to integrate the Deno language server with your editor:
// https://deno.land/manual/getting_started/setup_your_environment
// This enables autocomplete, go to definition, etc.

Deno.serve(async (req) => {
  const { url, prompts } = await req.json()
  const endpoint = "https://api.jigsawstack.com/v1/ai/scrape";
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": "sk_9717bc1ca31dd22d81dc47021ff2e45aeb8fc8ac5a4f97785aa4126bed3a8176b0552a6dc3de0e0cfeb16Ralx8SvvK0CiX9U", // Replace with your actual API key.
    },
    body: JSON.stringify({
      url: "https://gonzaga.campuslabs.com/engage/events",
      element_prompts: ["Event title", "Event time"],
    }),
    
  };

  const h2TextContent : string[] = [];

  // await fetch('https://gonzaga.campuslabs.com/engage/events')
  //     .then(response => response.text())
  //     .then(html => {
  //         // Create a temporary element to parse the HTML content
  //         // console.log(html.innerHTML)
  //         // let tempElement = document.createElement('div');
  //         // tempElement.innerHTML = html;

  //         // // Select all the <h2> tags
  //         // let h2Tags = tempElement.querySelectorAll('h2');

  //         // // Extract text content from each <h2> tag
  //         // h2Tags.forEach(h2 => {
  //         //     h2TextContent.push(h2.textContent.trim()); // Trim to remove extra spaces
  //         // });

  //         // // Log the text content of all <h2> tags
  //         // console.log(h2TextContent);
          
  //     })

  const result = await fetch(endpoint, options);
  const data = await result.json();

  console.log(data)


  // const data = {
  //   message: `Hello ${name}!`,
  // }
  return new Response(
    JSON.stringify(h2TextContent),
    { headers: { "Content-Type": "application/json" } },
  )
  
})

/* To invoke locally:

  1. Run `supabase start` (see: https://supabase.com/docs/reference/cli/supabase-start)
  2. Make an HTTP request:

  curl -i --location --request POST 'http://127.0.0.1:54321/functions/v1/campus-events-scraper' \
    --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6ImFub24iLCJleHAiOjE5ODM4MTI5OTZ9.CRXP1A7WOeoJeXxjNni43kdQwgnWNReilDMblYTn_I0' \
    --header 'Content-Type: application/json' \
    --data '{"name":"Functions"}'

*/
