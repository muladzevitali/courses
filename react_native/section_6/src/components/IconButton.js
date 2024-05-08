import { Pressable, StyleSheet } from "react-native"
import { Ionicons } from '@expo/vector-icons'


const IconButton = ({ icon, color, onPress }) => {
    return (
        <Pressable
            onPress={onPress}
            style={({ pressed }) => [styles.iconContainer, pressed && styles.pressed]}>
            <Ionicons name={icon} size={24} color={color} />
        </Pressable>
    )
}

const styles = StyleSheet.create({
    iconContainer: {
        marginRight: 8
    },
    pressed: {
        opacity: .5
    }
})

export default IconButton