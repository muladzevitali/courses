import { StyleSheet, View, Text, Pressable } from 'react-native';



function GoalItem(props) {
    return (
        <View style={styles.goalItemContainer}>

            <Pressable
                onPress={props.onDeleteItem.bind(this, props.id)}
                android_ripple={{ color: '#210644' }}
                style={({pressed}) => pressed && styles.pressedItem}

            >
                <Text style={styles.goalItemText}>{props.text}</Text>
            </Pressable>
        </View>
    )
};

const styles = StyleSheet.create({
    goalItemContainer: {
        flex: 1,
        margin: 8,
        borderRadius: 6,
        backgroundColor: '#5e0acc',
    },
    pressedItem:{
        opacity: 0.5,
    }, 
    goalItemText: {
        color: 'white',
        padding: 8,

    }
});

export default GoalItem;