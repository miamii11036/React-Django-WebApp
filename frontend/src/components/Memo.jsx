import React from "react";
import "../styles/Memo.css";

function Memo({ memo, deleteMemo }) {
    const formattedDate = new Date(memo.created_at).toLocaleDateString("en-US")
    return (
        <div className="memo-container">
            <p className="memo-title">{memo.title}</p>
            <p className="memo-content">{memo.content}</p>
            <p className="memo-date">{formattedDate}</p>
            <button
                className="delete-button"
                onClick={() => deleteMemo(memo.id)}>
                Delete
            </button>
        </div>
    )
}

export default Memo;