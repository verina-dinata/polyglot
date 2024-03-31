import * as React from 'react';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea, Box, Button } from '@mui/material';
import PlayArrowIcon from '@mui/icons-material/PlayArrow';
import SentenceModal from './sentenceModal'

export default function WordCard(props) {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);


  const cnAudioID = "word-chinese-audio" + props.word.id;
  const playChineseSound = (event) => {
    event.stopPropagation();
    const audioElement = document.getElementById(cnAudioID);
    audioElement.play();
  };

  const enAudioID = "word-english-audio" + props.word.id;
  const playEnglishSound = (event) => {
    event.stopPropagation();
    const audioElement = document.getElementById(enAudioID);
    audioElement.play();
  };

  const showSentencesPopup = (event) => {
    event.stopPropagation();
    handleOpen();
  };

  return (
    <Card sx={{ maxWidth: 345, minHeight: 200 }}>
      <audio preload={ "none" } id={ cnAudioID } src={ props.word.chinese_sound_path } hidden={true}></audio>
      <audio preload={ "none" } id={ enAudioID } src={ props.word.english_sound_path } hidden={true}></audio>

      <CardActionArea onClick={ playChineseSound }>
        <CardMedia
          component="div"
          height="140"
          // image="/static/images/cards/contemplative-reptile.jpg"
          alt="green iguana"
        >
          <Typography variant="h3" sx={{ textAlign: "center", p: 2, className: "noto-sans"}}>
            { props.word.word_string }
          </Typography>
        </CardMedia>
        <CardContent
          sx={{ minHeight: 150 }}
        >
          <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
            <Typography gutterBottom variant="h6" component="div">
              { props.word.pronounciation }
            </Typography>
            <PlayArrowIcon onClick={ playChineseSound } sx={{ '&:hover': { color: 'blue' } }} />
          </Box>

          <Typography variant="body2" color="text.secondary">
            { props.word.type }
          </Typography>
          <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
            <Typography variant="body2" color="text.secondary">
              { props.word.english_definition }
            </Typography>
            <PlayArrowIcon onClick={ playEnglishSound } sx={{ '&:hover': { color: 'blue' } }} />
          </Box>
        </CardContent>
        <Box p={1} sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center'}}>
          <Button sx={{ width: '100%' }} onClick={ showSentencesPopup } variant="contained">Examples</Button>
        </Box>
      </CardActionArea>
      <SentenceModal
        open={ open }
        handleClose={ handleClose }
        word={ props.word }
        playChineseSound={ playChineseSound }
        playEnglishSound={ playEnglishSound }
      />
    </Card>
  );
}
