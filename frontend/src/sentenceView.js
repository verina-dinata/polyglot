import { Box, Grid, Typography } from "@mui/material";
import PlayArrowIcon from '@mui/icons-material/PlayArrow';


export default function SentenceView(props) {
  const cnAudioID = "sentence-chinese-audio" + props.sentence.id;
  const playChineseSound = (event) => {
    event.stopPropagation();
    const audioElement = document.getElementById(cnAudioID);
    audioElement.play();
  };

  const enAudioID = "sentence-english-audio" + props.sentence.id;
  const playEnglishSound = (event) => {
    event.stopPropagation();
    const audioElement = document.getElementById(enAudioID);
    audioElement.play();
  };


  return (
    <Box>
      <audio preload={ "none" } id={ cnAudioID } src={ props.sentence.chinese_sound_path } hidden={true}></audio>
      <audio preload={ "none" } id={ enAudioID } src={ props.sentence.english_sound_path } hidden={true}></audio>
      <Typography variant="h6">
        ___________________________________
      </Typography>
      <Typography>
        { props.sentence.sentence_string }
      </Typography>
      <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'space-between' }}>
        <Typography id="modal-modal-description">
          { props.sentence.pronounciation }
        </Typography>
        <PlayArrowIcon onClick={ playChineseSound } sx={{ '&:hover': { color: 'blue' } }} />
      </Grid>
      <Grid item xs={12} sx={{ display: 'flex', justifyContent: 'space-between' }}>
        <Typography id="modal-modal-description">
          { props.sentence.english_translation }
        </Typography>
        <PlayArrowIcon onClick={ playEnglishSound } sx={{ '&:hover': { color: 'blue' } }} />
      </Grid>
    </Box>
  )
}
