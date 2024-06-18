import { View, Alert, Image, Text, StyleSheet } from "react-native"
import { launchCameraAsync, useCameraPermissions, PermissionStatus } from 'expo-image-picker'
import { useState } from "react"
import { Colors } from "../../constants/colors"
import OutlineButton from "../UI/OutlineButton"


const ImagePicker = ({ onTakeImage }) => {
    const [cameraPermissionInformation, requestPermission] = useCameraPermissions()
    const [pickedImage, setPickedImage] = useState()

    const verifyPermission = async () => {
        if (cameraPermissionInformation.status === PermissionStatus.UNDETERMINED) {
            const permissionResponse = await requestPermission()
            return permissionResponse.granted
        } else if (cameraPermissionInformation.status === PermissionStatus.DENIED) {
            Alert.alert('Insufficient permissions', 'You need to grant camera permissions to use this app')
            return false
        }
        return true

    }

    const takeImageHandler = async () => {
        const isGranted = await verifyPermission()
        if (!isGranted) {
            return
        }

        const image = await launchCameraAsync({
            allowEditing: true,
            aspect: [16, 9],
            quality: .5
        });

        setPickedImage(_ => image.assets[0].uri)
        onTakeImage(image.assets[0].uri)
    }

    let imagePreview = <Text>No image taken yet</Text>
    if (pickedImage) {
        imagePreview = <Image source={{ uri: pickedImage }} style={styles.image} />
    }
    return (
        <View>
            <View style={styles.imagePreview}>
                {imagePreview}
            </View>
            <OutlineButton onPress={takeImageHandler} icon='camera'>Take image</OutlineButton>
        </View>
    )
}

const styles = StyleSheet.create({
    imagePreview: {
        width: '100%',
        height: 200,
        marginVertical: 8,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: Colors.primary100,
        borderRadius: 4,
        overflow: 'hidden'
    },
    image: {
        width: '100%',
        height: '100%',
        borderRadius: 4
    }
})

export default ImagePicker