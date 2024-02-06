// Follow this setup guide to integrate the Deno language server with your editor:
// https://deno.land/manual/getting_started/setup_your_environment
// This enables autocomplete, go to definition, etc.

Deno.serve(async (req) => {
  console.log(Deno.env.get("AI_TOKEN"))
  const { url, prompts } = await req.json()
  const endpoint = "https://api.jigsawstack.com/v1/ai/scrape";
  const options = {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "x-api-key": Deno.env.get("AI_TOKEN"),
    },
    body: JSON.stringify({
      url: url,
      element_prompts: prompts,
    }),
    
  };

  console.log(options)

  const result = await fetch(endpoint, options);
  const data = await result.json();

  console.log(data)


  // const data = {
  //   message: `Hello ${name}!`,
  // }
  return new Response(
    JSON.stringify(data),
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
