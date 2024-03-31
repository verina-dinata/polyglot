import { Box, Button, Card, Container, Paper, Typography } from "@mui/material";
import WordList from "./wordList";

function App() {
  return (

    <Container>
      <Typography variant="h1" sx={{ my:4, textAlign: "center", color: "primary.main" }}>
        1000 Frequent Words
      </Typography>
      <WordList></WordList>
    </Container>
  )
}

export default App;
