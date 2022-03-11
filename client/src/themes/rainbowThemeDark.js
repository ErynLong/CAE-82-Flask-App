import { createTheme } from '@mui/material/styles';

const themeOptions = 
{
      components:{   
        MuiAppBar:{
          styleOverrides:{
            colorPrimary:{
              backgroundImage:`linear-gradient(0deg, #33333375, #33333375 100%),
              linear-gradient(120deg,
                rgba(255, 0, 0, 1) 0%,
                rgba(255, 154, 0, 1) 10%,
                rgba(208, 222, 33, 1) 20%,
                rgba(79, 220, 74, 1) 30%,
                rgba(63, 218, 216, 1) 40%,
                rgba(47, 201, 226, 1) 50%,
                rgba(28, 127, 238, 1) 60%,
                rgba(95, 21, 242, 1) 70%,
                rgba(186, 12, 248, 1) 80%,
                rgba(251, 7, 217, 1) 90%,
                rgba(255, 0, 0, 1) 100%
            )
                
            ` 
            }
          }
        }
    },

    palette: {
      type: 'dark',
      mode:'dark',
      primary: {
        main: '#f50057',
      },
      secondary: {
        main: '#BE0AFF',
      },
      warning: {
        main: '#DEFF0A',
      },
      info: {
        main: '#147DF5',
      },
      success: {
        main: '#A1FF0A',
      },
      background: {
        paper: '#BD2C16',
        default: '#4E0D14',
      },
      divider: '#FF8700',
    },
    typography: {
      caption: {
        fontSize: '6rem',
      },
      button: {
        fontWeight: 500,
      },
    },
    props: {
      MuiTooltip: {
        arrow: true,
      },
    },
    
  };

  const theme = createTheme(themeOptions);
  export default theme
  
