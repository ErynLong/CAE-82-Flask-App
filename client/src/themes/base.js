import rainbowTheme from './rainbowTheme'
import rainbowThemeDark from './rainbowThemeDark'

const themes ={
    rainbowThemeDark,
    rainbowTheme
}

export default function getTheme(theme){
    return themes[theme]
}