import  { useState, useEffect } from 'react';
import axios from 'axios';
import PropTypes from 'prop-types';
import { Box, Modal, Typography, Grid } from "@mui/material";
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';

import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import CloseIcon from '@mui/icons-material/Close';
import SentenceView from './sentenceView';


const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

export default function SentenceModal(props) {
  const apiUrl = "http://localhost:3000/api/v1/words/" + props.word.id + "/sentences";
  const [sentences, setSentences] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);



  useEffect(() => {
    const fetchSentences = async () => {
      if (sentences.length === 0 && props.open === true){
        try {
          const response = await axios.get(apiUrl);
          console.log(response.data)
          setSentences(response.data);
        } catch (error) {
          setError(error);
        } finally {
          setIsLoading(false);
        }
      }
    };

    fetchSentences();
  }, [props.open, sentences]);


  return (
    <Modal
      open={props.open}
      onClose={props.handleClose}
      aria-labelledby="modal-modal-title"
      aria-describedby="modal-modal-description"
    >
      <Box sx={style}>
        <Grid container spacing={1}>
          <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'space-between' }}>
            <Typography id="modal-modal-title" variant="h1" component="h1">
              { props.word.word_string }
            </Typography>
            <CloseIcon onClick={ props.handleClose } />
          </Grid>
          <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'space-between' }}>
            <Typography id="modal-modal-description">
              { props.word.pronounciation }
            </Typography>
            <PlayArrowIcon onClick={ props.playChineseSound } sx={{ '&:hover': { color: 'blue' } }} />
          </Grid>
          <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'space-between' }}>
            <Typography id="modal-modal-description">
              { props.word.english_definition }
            </Typography>
            <PlayArrowIcon onClick={ props.playEnglishSound } sx={{ '&:hover': { color: 'blue' } }} />
          </Grid>

          <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'space-between' }}>

            <Box>
              {
                sentences.map((sentence) => (
                  <SentenceView sentence={ sentence }></SentenceView>
                ))
              }
            </Box>
          </Grid>
        </Grid>

        {/* <Typography id="modal-modal-description" sx={{ mt: 2 }}>
          {props.word.pronounciation}
          <PlayArrowIcon onClick={ props.playChineseSound } sx={{ '&:hover': { color: 'blue' } }} />
        </Typography>
        <Typography id="modal-modal-description" sx={{ mt: 2 }}>
          {props.word.english_definition}
          <PlayArrowIcon onClick={ props.playEnglishSound } sx={{ '&:hover': { color: 'blue' } }} />
        </Typography> */}

        {/* <Box>
          {
            sentences.map((sentence) => (
              <Typography>
                { sentence.sentence_string }
                { sentence.pronounciation }
                { sentence.english_translation }
              </Typography>
            ))
          }
        </Box> */}
      </Box>
    </Modal>
  )
}
