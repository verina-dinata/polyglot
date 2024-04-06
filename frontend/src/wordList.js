import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Box, Grid, Pagination } from "@mui/material";
import WordCard from "./wordCard";

export default function WordList() {

  // const apiUrl = 'https://lfh3knfmaxll3zix73xlj4wib40chwhw.lambda-url.ap-southeast-1.on.aws/api/v1/words';
  const apiUrl = '/api/v1/words';
  const [words, setWords] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages] = useState(28);

  useEffect(() => {
    const fetchWords = async () => {
      try {
        console.log(currentPage)
        const response = await axios.get(`${apiUrl}?page=${currentPage}`);
        setWords(response.data);
      } catch (error) {
        setError(error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchWords();
  }, [currentPage]);

  const handlePageChange = (e, p) => {
    setCurrentPage(p);
  };

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: '10px'}}>
        <Pagination count={totalPages} color="secondary" onChange={handlePageChange} />
      </Box>
      <Grid container spacing={2} sx={{ marginBottom: '30px' }}>
        {isLoading ? (
          <p>Loading words...</p>
        ) : error ? (
          <p>Error fetching words: {error.message}</p>
        ) : (
          words.map((word) => (
            <Grid item xs={6} md={3} lg={2} key={word.id || word.name}> {/* Use a unique key for each word */}
              <WordCard word={word} /> {/* Pass the word object to WordCard */}
            </Grid>
          ))
        )}
      </Grid>
      {/* <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: '10px'}}>
        <Pagination count={totalPages} color="secondary" onChange={handlePageChange} />
      </Box> */}
    </Box>
  )
}
