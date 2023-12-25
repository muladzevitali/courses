export default function TabButton({children , isSelected, ...props}) {

    return (
        <li>
            <button className={isSelected === true ? "active": undefined} {...props}>{children}</button>
        </li>
    )
}