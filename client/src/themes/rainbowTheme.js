import { createTheme } from '@mui/material/styles';


const themeOptions = 
{
      components:{   
        MuiAppBar:{
          styleOverrides:{
            colorPrimary:{
              backgroundImage:`linear-gradient(120deg,
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
            )` 
            }
          }
        }
    },

    palette: {
      mode: 'light',
      type: 'light',
      primary: {
        main: '#BE0AFF',
      },
      secondary: {
        main: '#f50057',
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
      divider: '#FF8700',
    },
    props: {
      MuiTooltip: {
        arrow: true,
      },
    },
    
  };

  const theme = createTheme(themeOptions);
  
  export default theme