import { Box, Button, Container, Paper, Typography } from "@mui/material";


const serviceList = ["Service 1", "Service 2", "Service 3"]
function App() {
  return (
    // <Container sx={{ bgcolor: 'tomato', height: '100vh'}}>
    //   <Typography sx={{ p: 1 }}>Hello World</Typography>
    // </Container>

    <Container>
      <Typography variant="h1" sx={{ my:4, textAlign: "center", color: "primary.main" }}>
        Services
      </Typography>
      <Typography variant="h2">
        Overiew
      </Typography>
      <Box
        sx={{
          pt: 4,
          display: 'flex',
          flexDirection: { xs: "column", md: "row"},
          justifyContent: "space-between",
          gap: 4,
          }}
      >
        {serviceList.map((service) => (
          <Paper elevation={3} sx={{ width: {xs: 1, md: 320}}}>
            <Box sx={{ m:3 }}>
              <Typography variant="h3">{service}</Typography>
              <Typography sx={{ mt:2 }}>
              Lorem ipsum dolor sit amet, consectetur adipiscing elit. Phasellus a dolor aliquet, tincidunt tortor nec, gravida eros. Quisque pulvinar nunc non sapien imperdiet, ac tempus diam feugiat. Sed urna enim, ultrices et elementum vel, malesuada eu lacus. Nullam est orci, lobortis at
              </Typography>
              <Button variant="contained" color="secondary" sx={{ mt:2 }}>Learn more</Button>
            </Box>

          </Paper>
        ))}
      </Box>

    </Container>
  )
}

export default App;
