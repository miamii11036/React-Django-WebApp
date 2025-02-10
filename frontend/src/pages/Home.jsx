import { useState, useEffect } from "react";
import  api  from "../api";
import Memo from "../components/Memo";
import "../styles/Home.css";


function Home() {
    const [memo, setMemo] = useState([]);
    const [content, setContent] = useState("");
    const [title, setTitle] = useState("");

    useEffect(() => {
        getMemo();}, []);

    const getMemo = () => {
        api.get("api/memos/")
            .then((res) => res.data)
            .then((data) => {setMemo(data), console.log(data)})
            .catch((error) => alert(error));
    };

    const deleteMemo = (id) => {
        api.delete(`api/memos/delete/${id}`)
            .then((res) => {
                if (res.status === 204) {
                    alert("Delete success");
                } else {
                    alert("Delete failed");
                };
                getMemo();
            })
            .catch((error) => alert(error));
    };

    const createMemo = (e) => {
        e.preventDefault();
        api.post("api/memos/", {content, title})
            .then((res) => {
                if (res.status === 201) {
                    alert("Create success");
                } else {
                    alert("Create failed");
                };
                getMemo();
            })
            .catch((error) => alert(error));
        getMemo();
    }

    return (
        <div>
            <div>
                <h2>Create Memo</h2>
                <form onSubmit={createMemo}>
                    <label htmlFor="title">Title:</label>
                    <br />
                    <input 
                        type="text" 
                        id="title" 
                        name="title" 
                        required 
                        onChange={(e) => setTitle(e.target.value)}
                        value={title}
                    />
                    <br />
                    <label htmlFor="content">Content:</label>
                    <br />
                    <input 
                        type="text" 
                        id="content" 
                        name="content" 
                        required 
                        onChange={(e) => setContent(e.target.value)}
                        value={content}
                    />
                    <br />
                    <input type="submit" value="Submit" />
                </form>
            </div>
            <div>
                <h2>Memo</h2>
                {memo.map((memo) => 
                    <Memo key={memo.id} memo={memo} deleteMemo={deleteMemo} />)}
            </div>  
        </div>
    );
}

export default Home;