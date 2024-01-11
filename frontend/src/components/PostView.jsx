import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const PostView = () => {
    const { postId } = useParams();

    const [state, setState] = useState({
        comment: '',
        post: postId
    });
    const [post, setPost] = useState(null);
    const [focusedTextarea, setFocused] = useState(false);

    const getPost = async (id) => {
        let response = await axios.get('/api/getPost/', {
            params: {
                postId: postId
            }
        });

        return response.data
    }

    useEffect(() => {
        const postReciever = async () => {
            let post = await getPost();
            setPost(post);
        }

        postReciever();
    }, []);

    const setComment = (value) => {
        setState({
            ...state,
            comment: value
        })
    }

    const writingComment = () => {
        setFocused(true);
    }

    const addComment = async () => {
        console.log('Created comment');

        let response = await axios.post('/api/createComment/', state);
        console.log(response);
    }

    return (
        <>
            <h1>{post ? post.title : 'Loading...'}</h1>
            {post && (
                <>
                <p>Written on {post.timestamp}</p>

                <p>{post.content}</p>

                {
                    post.comments.map(comment => {
                        <p>{comment}</p>
                    })
                }
                </>
                )
            }

            <textarea value={state.comment} onFocus={writingComment} onChange={(e) => setComment(e.target.value)} placeholder='Leave a comment' cols="30" rows="10" />

            {focusedTextarea && (
                <button onClick={addComment}>Submit</button>
            )
            }
        </>
    )
}

export default PostView;