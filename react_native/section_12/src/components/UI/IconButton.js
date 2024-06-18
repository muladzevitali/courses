import { Pressable, StyleSheet } from "react-native"
import { Ionicons } from '@expo/vector-icons'


const IconButton = ({ icon, size, color, onPress }) => {
    return <Pressable onPress={onPress} styles={({pressed}) => [styles.button, pressed && styles.pressed]}>
        <Ionicons name={icon} size={size} color={color} />
    </Pressable>
}


const styles = StyleSheet.create({
    button: {
        padding: 8,
        justifyContent: 'center',
        alignItems: 'center'
    },
    pressed: {
        opacity: .7
    }
})

export default IconButton