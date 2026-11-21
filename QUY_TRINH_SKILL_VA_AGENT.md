# Quy trình vận hành và agent theo dự án

**Phiên bản 3.0.2 — 22/11/2026.** Tài liệu triển khai năm quy trình HOST theo `AGENTS.md`; AGENTS là nguồn luật tác nghiệp chuẩn. Quy trình, template và adapter không được tự sinh authority hoặc nới quyền. Bộ tài sản chưa được cài hay nghiệm thu tại máy chỉ vì đã có trong ZIP.

Khi task hiện hành giao chuyển nguồn, thực hiện đúng loại tác động và phạm vi ở task đó. Workflow này mô tả cách làm. Quyền soạn, thử, chuyển hoặc phục hồi được đối chiếu riêng ở nguồn Owner và cổng dự án.

## 1. Nguồn và nơi triển khai

| Thành phần | Nơi dùng và giới hạn |
|---|---|
| Luật chung | `AGENTS.md`; Claude nhập cùng nguồn qua `CLAUDE.md` với `@AGENTS.md` |
| Cây/task/findings | Nguồn hiện có của từng dự án; không lập STATE/ROADMAP/registry cạnh tranh |
| Điểm gọi skill native | `.agents/skills/<ten-skill>/SKILL.md` dẫn vào đúng mục 4–8 đã bind. Mở repo ứng viên trong client đã được phép để kiểm discovery. Mục 4–8 là một nguồn thao tác |
| Skill Codex tại repo | `.agents/skills/<ten-skill>/SKILL.md` theo client thực [O1] |
| Điểm tìm skill Claude | `.claude/skills/<ten-skill>/`; nối cùng nguồn hoặc bản sinh được kiểm khớp [O2] |
| Profile worker | Codex `.codex/agents/<du-an>-<vai>.toml`; Claude `.claude/agents/<du-an>-<vai>.md` [O3–O4] |
| Danh tính HOST | Nhật ký hiện có ngoài canonical authority khi dự án đòi trung lập nhà cung cấp |
| Claim/receipt/custody | Registry, helper, checkpoint/index và retention thật của dự án |
| Bản gửi ChatGPT | Mỗi dự án có `Gui_ChatGPT_<Ten_du_an>.md` cùng cây khớp revision theo R19; không cần ChatGPT để chạy hay nhả task |

Tìm skill/profile đang phục vụ đúng trigger trước khi cài. Nếu dùng skill native, dùng điểm gọi tới đúng mục đã bind; xác minh client mở và đọc nguồn thao tác thật. Đối chiếu phiên bản, import, override, trust và discovery trên client thật. Claude Code hỗ trợ `@AGENTS.md` cùng thư mục. Khả năng đọc trực tiếp phụ thuộc phiên bản và chế độ, kiểm trên phiên thực tế [O5]. Dùng đường đọc workflow đã bind khi native skill chưa được xác minh. Kiểm giới hạn byte nạp cộng dồn của Codex và phần cuối tài liệu tại root cùng thư mục con [O10].

Skill trong gói là workflow HOST. Giữ entitlement, quyền dữ liệu, sandbox và cổng sản phẩm của dự án. Nếu dự án yêu cầu trung lập công cụ, ghi định danh client/model/phiên ở task HOST và nối bằng ID trung lập.

## 2. Hợp đồng chung và danh tính

Coordinator tự lấy đầu vào từ cây/task/nguồn hiện hành; không bắt Owner điền biểu mẫu:
```text
Project / root-worktree / revision cây / mục tiêu và task:
Work unit / operation / predecessor theo lifecycle thật:
Vai trò / phạm vi đọc-ghi / baseline / quyết định hiệu lực:
Acceptance / thành tựu cần giữ / bằng chứng đã có và còn thiếu:
Nguồn quyền / tổng budget đã cấp, đã dùng, còn lại / tài nguyên:
Identity HOST / checkpoint và nơi nhận bàn giao / bước tiếp:
```

Worker trả kết quả vào scope được giao hoặc cho coordinator; đầu ra yêu cầu cập nhật cây không tự cấp quyền ghi sổ chung. Một đầu mối hợp nhất trạng thái. Mỗi quy trình trả kết quả, chứng cứ, phần thiếu và bước tiếp ngay trong sổ có sẵn; không file riêng cho từng lần gọi.

Claim/receipt/HANDOFF ánh xạ vào cơ chế thật, không là yêu cầu dựng schema mới. Dự án nhỏ dùng task/checkpoint sẵn có; nơi có lifecycle canonical bắt buộc thì ghi chú HOST không thay helper/receipt/release chuẩn.

Ngay khi nhận việc, **kể cả chỉ đọc**, phiên/worker tự cung cấp danh tính cho nhật ký HOST. Worker thiếu quyền ghi gửi ngay dữ kiện để coordinator có quyền ghi, không đợi cuối việc hoặc tự nới quyền.

| Trường danh tính | Cách ghi đúng |
|---|---|
| Công việc và vai | Project/task/work unit/operation, scope, vai và quan hệ cha nếu có |
| Công cụ và lần thực thi | Công cụ/client quan sát được; native session/thread/agent ID theo đúng loại; mã nội bộ ghi rõ là nội bộ |
| Cửa sổ | Ghi tên UI và native window ID tách riêng theo nguồn/thời điểm host cung cấp. Trường thiếu ghi NOT_EXPOSED. Nhãn tự đặt ghi riêng. Tên đổi được không làm khóa |
| Model/effort | Requested → configured → observed/effective; ghi nguồn và thời điểm, không lấy cấu hình làm bằng chứng turn đã đổi |
| Dấu vết tiếp quản | Checkpoint đủ byte, nơi bàn giao, receipt/own release và jobs còn sống |

Host không cung cấp trường nào thì ghi `NOT_EXPOSED`; chưa kiểm thì CHƯA XÁC MINH. Không tráo PID/session/thread/window, bịa API lấy ID hoặc bắt Owner tra hộ. Ghi identity nền một lần rồi delta khi nhận/chuyển việc, đổi tên/model/effort, checkpoint, lỗi, kết thúc; không tạo log riêng cho mỗi cửa sổ. Giữ alias cũ→mới theo lần quan sát; che dữ liệu bảo vệ trong tên nếu có.

## 2a. Nội dung cây và cách đọc theo R02

R15 áp dụng xuyên phiên. Đầu mối có quyền cập nhật ngay khi đổi người giữ hoặc phạm vi, có tiến độ, quyết định, lỗi, blocker, kết quả hay job thay đổi. Worker gửi delta ngay. Khi chưa nhập được, giữ delta và đầu mối trong task đang có, trỏ đúng revision, bằng chứng và bước tiếp.

Ánh xạ các nhóm sau vào **cây chuẩn và các sổ đang có**, không bắt đổi tên cây hoặc dựng thêm bảng dữ liệu cạnh tranh. Đây là cách triển khai R02/R15, không là nguồn luật độc lập. Với dự án nhỏ, các nhóm có thể nằm trong cùng một tệp; tên gợi ý khi chưa có nguồn tương đương là `CAY_DU_AN_<Ten_du_an>.md`. Cây chứa tóm lược đủ dùng và dẫn chi tiết, không chỉ là danh sách thư mục.

| Nhóm cần thấy trong cây hiện hành | Nội dung tối thiểu và giới hạn |
|---|---|
| Nhận diện và phạm vi | Project ID, root/worktree, revision, mốc cập nhật, nguồn luật, đầu mối cập nhật; mục tiêu và giai đoạn được phép. |
| Cấu trúc chức năng | Thành phần/chức năng chính, implementation chuẩn, caller/đường dùng, owner và phụ thuộc; phân biệt đang dùng, candidate và lịch sử. |
| Đã làm/đã đạt | Kết quả, đối tượng và revision đã kiểm, đường tới bằng chứng; tách đã xây, đã kiểm, đã tích hợp, đang dùng. Chưa nối không có nghĩa chưa xây. |
| Việc đang làm và bàn giao | Task/scope, người giữ, kết quả/phần dở, checkpoint, bước tiếp và mốc. Tại nút công việc ghi danh tính theo R15, gồm tên và native ID cửa sổ, session/thread/agent ID do host cung cấp; trường thiếu ghi NOT_EXPOSED. Nguồn đòi trung lập hoặc bảo vệ thông tin dẫn ref trung lập trực tiếp tới bản ghi HOST được phép. |
| Chưa làm/còn thiếu | Khoảng cách tới mục tiêu/tiêu chí, phụ thuộc và ưu tiên có căn cứ; phân biệt chưa làm với chưa khảo sát/chưa biết. |
| Vướng mắc | Vướng gì, ảnh hưởng task nào, bằng chứng, phụ thuộc/đầu mối xử lý, điều kiện hoặc bước gỡ được phép. |
| Lỗi và nghi vấn | ID ổn định, vị trí/phạm vi, ảnh hưởng, chứng cứ hoặc giả thuyết, trạng thái xác nhận/chưa kiểm/đã xử lý; liên kết finding trùng thay vì sinh mã khác. |
| Quyết định và bất biến | Quyết định còn hiệu lực, nguồn quyền, điều bị thay thế, thành tựu phải giữ, giai đoạn/quyền đang giới hạn. |
| Nhánh và tài sản | Candidate/thử nghiệm/nhánh bỏ, chủ, consumer, phần giữ/chuyển/dọn; điều kiện, quyền và phục hồi. Tên old/temp hoặc bị bỏ hướng không tự cấp quyền xóa. |
| Độ phủ hiểu biết | Phạm vi đã khảo sát, chưa khảo sát, đọc một phần, thiếu quyền, nguồn mâu thuẫn; định nghĩa mẫu số nếu có tỷ lệ. Không tự tính chưa đọc thành đã phủ. |
| Bước tiếp | Việc hợp lệ kế tiếp, lý do/phụ thuộc, người nhận hoặc trạng thái chưa có người nhận, tiêu chí, phép kiểm và phạm vi quyền. |

Mỗi nút có kết luận cần nối được trạng thái → nguồn/bằng chứng → revision/phạm vi áp dụng. Các nhóm có thể dùng chung một bảng; không cần tạo một file cho mỗi nhóm. Không có dữ kiện thì ghi CHƯA XÁC MINH hoặc trạng thái thích hợp cùng phần cần đọc tiếp. Phân biệt **đủ các mục hồ sơ**, **độ phủ khảo sát** và **mức đạt của sản phẩm**; không gộp thành một chữ ĐẦY ĐỦ/PASS.

**Cây chưa có hoặc đang dựng:** khởi tạo/bổ sung baseline tối thiểu từ nguồn đã đọc, giữ các khoảng chưa biết rõ ràng. Không ép agent đọc hết repository nhiều năm trước mọi công việc; giữ đúng phạm vi khám đã được giao. Nếu người khác đang hoàn thiện cây, đọc revision/checkpoint nhất quán, trả delta cho đầu mối đó hoặc nhận bàn giao qua lifecycle thật. Không làm cây thứ hai và không ghi đè bản đang cập nhật.

**Nhịp đọc:** coordinator mới/đổi AI/tiếp quản đọc toàn cây hiện hành; mỗi task kế tiếp cùng phiên kiểm revision và đọc phần liên quan/delta. Sau mất ngữ cảnh không phục hồi được dấu đọc thì đọc đủ lại. Dấu đọc trong nhật ký hiện có ghi nguồn/revision, phạm vi thực đọc và phần thiếu; output cắt phải đọc bù. Tóm tắt hoặc hash không thay thao tác đọc. Worker đọc đủ phạm vi cây được giao; trở thành coordinator phải đọc toàn cây.

**Giữ cây gọn mà không mất nghĩa vụ:** lịch sử kết thúc có thể tách với chỉ mục và đường phục hồi sau đối chiếu bảo toàn. Cây hiện hành vẫn giữ mọi quyết định còn hiệu lực, thành tựu có nguồn, lỗi mở, chủ/phụ thuộc, việc dở và giới hạn độ phủ. Chưa hoàn tất việc tách thì đọc cây hiện có; không đổi tên bản tóm tắt thiếu thành toàn cây.

Nếu cây đang được hoàn thiện, ghi phần đã đọc, độ phủ, việc dở và người đang giữ. Kiểm revision và quyền trước tác động. Giữ phạm vi người đang làm và đợi bàn giao hợp lệ để tiếp quản.

## 2b. Nối năm bước qua cùng task

Áp vòng R18. Mỗi bước dùng đầu ra của bước trước và ghi vào cây/task hiện có khi đạt mốc R15. Việc có rủi ro hoặc cổng review đi qua kiểm chéo. Mốc cập nhật được thực hiện ngay khi phát sinh và tiếp lại bước đang làm.

| Bước và skill | Dữ liệu cần chuyển |
|---|---|
| Tiếp nhận · tiep-quan-du-an | Project, luật, revision, người giữ, authority, checkpoint và phần đã chứng minh |
| Chọn đầu ra, làm và tự kiểm · thuc-hien-thay-doi | Đầu ra, scope, baseline, phép kiểm rẻ, diff và chứng cứ. Một lượt sửa lỗi cần căn cứ hoặc phép kiểm phân biệt theo R13 |
| Kiểm chéo · kiem-chung-va-loi-ngam | Current diff, bằng chứng đúng target, finding và tác động. Chỉ tiếp delta có căn cứ |
| Cập nhật · cap-nhat-va-ban-giao (nhánh tiến độ) | Delta cây/task, quyền, snapshot và phần PENDING. Cập nhật xong tiếp bước đang làm |
| Khép hoặc chuyển quyền · cap-nhat-va-ban-giao (nhánh kết thúc) | Checkpoint đọc lại được, kết quả dọn nếu cần, receipt/trạng thái nhả, người tiếp và việc còn hợp lệ |

Đổi luật hoặc binding dùng thủ tục migration ở mục 9. Đầu phiên xác minh nguồn và đọc cây theo vai. Trong từng task dùng vòng trên, delta theo revision và cổng đúng phạm vi. Nguồn skill chưa được client xác nhận thì dùng quy trình tương đương được phép ở mục 4–8.

## 3. Ba vai theo dự án, mức suy nghĩ và ngân sách

| Vai | Trách nhiệm | Ranh giới |
|---|---|---|
| `<du-an>-viet-ma` | Một phần hành vi chạy được, sửa đúng owner, tự kiểm, checkpoint và khép scope | Không tự nhận review độc lập diff mình viết |
| `<du-an>-kiem-chung` | So yêu cầu/baseline/target/bằng chứng, kiểm finding và hồi quy liên quan | Không sửa source coder hoặc oracle để tạo PASS |
| `<du-an>-soi-loi-ngam` | Giả thuyết về ranh giới, trạng thái lỗi, hủy/retry, dữ liệu/quyền/chi phí | Không quét toàn kho vô hạn, bịa lỗi hoặc tự mở scope |

Coordinator là phiên giữ việc, không cần worker thứ tư chỉ để ghi sổ. Vai tái dùng lâu dài; tiến trình worker chạy khi có task rồi kết thúc, không canh rỗng. Chọn có cần reviewer độc lập và soi lỗi ngầm theo R08. Dùng vai đang có phù hợp với quyền và ngân sách; không giao một agent cho mỗi file, setup hoặc lớp kỹ thuật.

Hai worker cùng đọc được trong quyền; cùng ghi phải tách scope hoặc tuần tự. Worktree không tự cách ly database, port, secret, cloud job. Reviewer “chỉ đọc” phải được ràng buộc bằng quyền/tool/sandbox host và thử ca từ chối; prompt/frontmatter không tự cưỡng chế. Test cần ghi chỉ dùng vùng thử được cấp. Không dùng memory cá nhân chứa trạng thái xuyên dự án.

Đối chiếu B và mức Owner đặt cho cửa sổ giao việc theo R09. Agent con chọn mức host hỗ trợ theo phần việc, không sao chép mức của phiên cha mặc định. Mức nhẹ/vừa hoặc cao/chuyên sâu là nhóm theo độ khó, không phải tên cứng cho mọi client. Nếu host không có hoặc không expose lựa chọn riêng, ghi đúng giới hạn; dùng tuyến còn hợp lệ trong quyền và ngân sách. Khi đổi cửa sổ/công cụ giữ checkpoint và accounting.

Đối chiếu default/profile/UI/phiên lưu/override/fallback thực. Bỏ trường model không bảo đảm kế thừa; cấu hình bắt buộc chưa xác nhận thì chưa dispatch phần cần nó. Ghi effective khi host cung cấp; không bịa mức không expose, ánh xạ ngầm mức không hỗ trợ hoặc hồi tố thay đổi cho turn đang chạy.

**Tổng ngân sách theo mục tiêu** lấy từ quyền/hạn mức hiện hành hoặc ủy quyền xác lập giới hạn có nguồn. Chưa có con số nhưng được ủy quyền thì chốt một tổng trần hữu hạn theo thời gian/phép thử, ghi căn cứ; tính cả coder, reviewer, lỗi, inflight, cleanup qua mọi phiên/công cụ/task ID. Mỗi batch có trần quan sát được trong phần còn lại; chia nhỏ không gia hạn tổng budget. Giữ phần cần cho dừng/khép tài nguyên trong giới hạn, không tự cấp “mức thường lệ” khi chưa có căn cứ.

Credits không đo được thì ghi CHƯA ĐO, dùng trần thời gian/phép thử/concurrency được phép; không coi đó là chi mở. Chạm giới hạn giữ checkpoint/nghĩa vụ và bước có căn cứ; không tăng trần, đổi ID hoặc gọi hết budget là PASS/TASK_FAIL. Làm phần độc lập đã được phép, chỉ hỏi đúng quyền/quyết định thật sự thiếu.

## 4. Skill `tiep-quan-du-an`

**Trigger:** coordinator mới, đổi Codex↔Claude/workspace, gián đoạn hoặc mất ngữ cảnh đáng tin. **Không làm lại toàn quy trình:** câu hỏi nhỏ trong cùng phiên; worker chỉ nhận scope cục bộ.

1. Nhận project/root/cây và chuỗi luật thực nạp; tự ghi identity HOST. Đọc nguồn current, không chọn authority theo timestamp hoặc memory.
2. Coordinator đọc **toàn cây hiện hành một lần** và luật áp dụng; chia đoạn, đọc bù output cắt/dòng dài. Ghi revision/phần thiếu; che mất logic cũng là chưa đọc đủ. Hash, grep hoặc tóm tắt không chứng minh đọc trọn.
3. Trước task kế tiếp cùng phiên kiểm revision, đọc phần liên quan/delta và quan hệ bị ảnh hưởng. Sau compaction đối chiếu dấu đọc/revision/task; không phục hồi đáng tin thì đọc đủ lại. Worker đọc đủ scope được giao; thành coordinator phải đọc toàn cây.
4. Đối chiếu các nhóm nội dung cây theo mục 2a, ghi đúng phần thiếu/đang được hoàn thiện và người giữ. Lấy mục tiêu, mốc dùng được, đã/đang/sẽ làm, quyết định, owner/caller, findings và tài sản. Giữ kết quả có chứng cứ theo revision/phạm vi; chưa nối/candidate/thiếu quyền chạy không có nghĩa chưa xây.
5. Đối chiếu base/current, staged/unstaged/untracked, byte ngoài Git, claim/writer/jobs/chi phí và quyền. Tìm checkpoint qua index/lifecycle; không tự xóa lock ngoại lai hoặc suy job chết vì đóng cửa sổ.
6. Nhận cùng lineage, attempt/budget và tác động không được replay; lifecycle cần operation kế nhiệm thì nối predecessor. Chuyển máy phục hồi đủ byte, không chỉ đường dẫn của máy cũ.
7. So lệnh theo mục tiêu/đối tượng/hiệu ứng/tiêu chí/quyết định: đã đạt, đang làm, mới, kiểm lại hợp lệ, tiền đề sai hoặc đổi ý. Báo sai/lặp có căn cứ, làm phần hợp lệ.
8. Chọn bước đang chặn **mốc sử dụng/nghiệm thu đã giao**, theo phụ thuộc và quyền; không mở audit/refactor mới chỉ vì còn có thể kiểm thêm. Báo ngắn rồi thực hiện.

Đọc cây không có nghĩa đọc lại toàn repo/ZIP/lịch sử/bằng chứng. Chỉ mở chứng cứ mà hành động phụ thuộc hoặc đang tranh chấp; giữ carry-forward hợp lệ, không chạy lại chỉ để yên tâm. Nghĩa vụ fresh-reopen tại gate dự án vẫn thực hiện; không mở dữ liệu cấm để đạt coverage.

**Đầu ra/xong:** nhận đúng việc không tranh writer, checkpoint phục hồi được, thành tựu/giới hạn và bước tiếp rõ. Phần thiếu giữ đúng trạng thái; tiếp đọc bù/phần không phụ thuộc trong quyền.

## 5. Skill `thuc-hien-thay-doi`

**Trigger:** phát triển, sửa lỗi, đổi hướng hoặc thay hợp đồng/cấu hình. **Không áp nguyên quy trình:** giải thích không sửa, chỉnh chữ nhẹ; chọn kiểm đúng mức.

1. So yêu cầu với việc đã đạt/đang làm và quyết định mới; tìm owner/caller/test/candidate/lịch sử liên quan. Dùng lại → nối → hoàn thiện/sửa đúng nơi. Chỉ thêm chủ sở hữu hoặc thành phần khi có trách nhiệm riêng, điểm tích hợp và vòng đời có căn cứ theo R06.
2. Đổi ý thì ghi phần giữ/thay/bỏ, acceptance và quyết định bị thay; dừng writer cũ trước giao lại. Kết quả muộn của task đã hủy không tự merge/promote.
3. Chọn **một lát cắt hành vi quan sát được trên đường dùng thật**: từ đầu vào qua owner/caller đến kết quả. Ghi baseline, scope, bất biến, integration point và cách kiểm. Không chia riêng agent cho từng setup/file/layer rồi để phần tích hợp cuối cùng chưa có chủ.
4. Trước sửa lỗi, lập giả thuyết và phép kiểm phân biệt nguyên nhân. Khi an toàn/khả thi, chứng minh phép kiểm bắt được lỗi gốc trước sửa; nếu không, giữ bằng chứng và giới hạn, dùng phản ví dụ phù hợp. Không ép TDD cho mọi thay đổi hoặc xóa mã đúng chỉ vì test được viết sau.
5. **Phản hồi rẻ trước:** kiểm hẹp bắt lỗi nhanh, rồi kiểm hồi quy theo ảnh hưởng và đường tích hợp thật. Không chạy toàn bộ lặp vô cớ, cũng không dùng kiểm hẹp thay gate/broad regression bắt buộc.
6. **Lỗi lặp:** đối chiếu harness/oracle, fixture/tài sản tạm, process cũ, cache/build artifact, root/config/version/quyền/môi trường trước bẻ hành vi sản phẩm. Không đổi expected, vô hiệu assertion hoặc ghim hash để làm đẹp.
7. Sửa một phần có thể kiểm; mỗi vòng thêm thông tin/loại giả thuyết/tiến bộ thật. Hai vòng không tiến bộ thì đổi cách chẩn đoán, không tạo vN hoặc mở agent trùng. Mọi vòng dùng cùng tổng budget.
8. Gắn kết quả với input được phép/thực chạy, target bytes/artifact và môi trường. Nếu R08 gọi kiểm chéo, chuyển yêu cầu, diff test/config và chứng cứ gốc sang mục 6.
9. Tích hợp trong quyền, kiểm phần tương tác trên bản hợp nhất, giữ sửa đúng. Đạt đơn vị việc thì chuyển một lần sang nhánh kết thúc ở mục 7.

**Đầu ra/xong:** hành vi hoặc patch đúng mức yêu cầu; bằng chứng/review, bất biến được giữ và phần chưa tích hợp/triển khai rõ. Lỗi ngoài scope ghi backlog, chỉ chặn nếu thực sự chặn mục tiêu/hồi quy; không biến task nhỏ thành sửa toàn dự án.

## 6. Skill `kiem-chung-va-loi-ngam`

**Trigger:** R08 xác định có cổng bắt buộc hoặc rủi ro đáng kể; kiểm lại finding trong cùng review theo R12. Giữ đúng target và phần bị ảnh hưởng.

1. Nhận project/task, yêu cầu, baseline, target revision/artifact, diff, acceptance và quyền; tự ghi identity. Reviewer khác coder của diff; đổi tên hoặc model không tạo tính độc lập. Đọc yêu cầu trước diễn giải thành công.
2. So đường dùng thật, owner/caller và phần đã bỏ/đổi; tách source/candidate/installed. Kiểm input được phép với input thực, assertion/mock/skip/xfail/0 ca và oracle có tự lấy output làm expected không.
3. Tự chạy kiểm phù hợp ở vùng an toàn hoặc đối chiếu bằng chứng gốc còn áp dụng. Chỉ đọc source thì kết luận review tĩnh, không runtime PASS. Không sửa source coder hoặc lấy dữ liệu bảo vệ làm đầu vào sửa.
4. Chọn giả thuyết lỗi ngầm theo vùng chạm: schema/đơn vị; dữ liệu/restore; hủy/retry/ghi muộn; tenant/quyền; UI/game/save-load; job/chi phí; AI/holdout; artifact/rollout. Không bắt mọi task kiểm mọi nhóm.
5. Finding có vị trí/đối tượng, điều kiện, ảnh hưởng, chứng cứ hoặc phép kiểm phân biệt. Tách hồi quy, lỗi cũ chặn mục tiêu, ngoài scope và nghi vấn; sở thích trình bày không tự chặn.
6. Coder sửa hoặc trả phản chứng. Reviewer xác minh finding đã được giải và **delta cụ thể cùng hồi quy liên quan**, không mở lại phần không đổi. Bất đồng giải bằng phép kiểm/nguồn đúng, không biểu quyết.
7. Ghi kết luận đúng mức: ĐẠT/KHÔNG ĐẠT/CHƯA CHẠY/BỊ CHẶN/MỘT PHẦN/KHÔNG ÁP DỤNG có lý do. Zero tests, timeout, skip, thiếu output hoặc hết budget không thành PASS.

Áp thủ tục review của nguồn dự án đang có hiệu lực. Review staging dùng cho delta đang soạn. Áp thủ tục kế nhiệm sau khi đạt điều kiện chuyển và xác nhận nguồn đó active.

Acceptance/phát hành, protected-evaluation, quyền và các cổng sản phẩm khác vẫn theo nguồn có hiệu lực, trừ đúng delta được giao. Chưa kích hoạt xong thì khép bước migration liên quan trước tác động phụ thuộc; không bỏ gate hoặc dùng ghi chú HOST thay authority.

**Đầu ra/xong:** kết luận và finding có chứng cứ, target được đối chiếu, lượt/budget ghi đúng; không cần tuyên không còn mọi lỗi tương lai. Giữ review/bằng chứng không đổi còn áp dụng, không bắt reviewer mới chạy lại toàn bộ.

## 7. Skill `cap-nhat-va-ban-giao`

**Cập nhật tiến độ.** Khi có mốc R15/R19, ghi một delta vào nguồn được quyền cập nhật. Worker thiếu quyền gửi ngay cho writer; task hiện có giữ revision, delta và đầu mối nếu PENDING. Writer so quyết định, quyền, claim/epoch, phiên bản và nguồn ngay tại commit. Cập nhật cây và packet tại hai đường dẫn đã bind. Đối chiếu manifest snapshot, nội dung điều phối được phép, phần chưa xác minh và đọc lại sau ghi. Packet tóm tắt hiện trạng, không chép cả cây hay dữ liệu protected. Khi nguồn đổi, quyền thiếu hoặc cặp ghi dở, giữ chứng cứ snapshot tốt bằng custody hiện có, đánh dấu PENDING và từ chối dùng cặp lệch để tiếp quản. Atomic replace một tệp không chứng minh cặp hai tệp đã nhất quán. Cập nhật xong thì tiếp bước đang làm.

**Khép hoặc chuyển quyền.** Chỉ nhánh này điều phối receipt và nhả quyền theo R16/R22, qua lifecycle đang áp dụng.

1. Ghi kết quả, việc dở, ngân sách/lượt thử, job, người giữ và bước tiếp. Bàn giao ngay khi phần việc được giao khép, kể cả worker chỉ đọc. Dùng nút cây và checkpoint theo R15 để phiên nhận đi thẳng tới nguồn bền. Worker không tự ghi chồng cây; lưu delta danh tính và kết quả qua kênh task hiện có đã được phép, ghi đầu mối nếu PENDING. Ngăn tác động ghi mới trong vùng bàn giao. Lưu rồi đọc lại checkpoint đủ staged/unstaged/untracked và tài sản ngoài Git cần phục hồi. Giữ logical ref, custody và điều kiện lấy lại ngoài worktree có thể dọn.
2. Nếu có tài sản hoặc job cần xử lý, dùng mục 8 rồi nhận kết quả dọn, giữ hoặc chuyển giao. Chốt người chịu trách nhiệm cho phần còn mở. Cập nhật cây/packet theo mốc đã xác minh; nếu nguồn có writer khác, lưu delta PENDING và đầu mối trong checkpoint.
3. Nếu đạt terminal, ghi một completion receipt bằng helper hiện có. Nếu còn dở, pause/transfer theo lifecycle thật và giữ work unit; không đánh dấu COMPLETED giả. Nếu đã có receipt khớp, đối soát thay vì ghi lại hoặc replay. Nhả ngay quyền của mình sau khi đạt điều kiện. Bàn giao bền không đợi người nhận mở cửa sổ. Người nhận tìm từ nút cây, task/checkpoint và lifecycle thay vì nhờ Owner truy phiên cũ.
4. Kiểm lifecycle sau nhả. Chỉ báo RELEASED khi có căn cứ thực. Nếu vẫn còn claim, ghi rõ chờ nhả hoặc CHỜ ĐỐI SOÁT. Writer đã nhả không ghi bằng quyền cũ. Phần trạng thái cây/packet sau nhả do đầu mối có quyền nhập từ delta và chứng cứ lifecycle. Báo riêng kết quả chuyên môn, quyền bàn giao và job/chi phí còn mở. Tiếp phần hợp lệ còn được giao.

| Điểm gián đoạn | Tiếp quản đúng |
|---|---|
| Checkpoint ghi dở | Giữ snapshot đã xác minh; đối chiếu byte chưa seal |
| Ghi cây xong, packet chưa xong | Giữ PENDING; từ chối cặp lệch, chỉ writer hợp lệ tiếp đúng delta |
| Bàn giao bền, receipt chưa xong | Khép bước còn thiếu; không replay tác động đã xác minh |
| Receipt bền, claim chưa nhả | Recovery có quyền đối soát receipt, claim và liveness; không nhả claim ngoại lai |
| Release xong, cây/packet còn cũ | Đầu mối có quyền nhập delta, lấy trạng thái thật từ lifecycle. Không suy ACTIVE từ log cũ |
| Worker cũ ghi muộn | Kiểm quyền và revision tại commit. Từ chối ghi bằng quyền cũ |

## 8. Skill `ket-thuc-nhanh-va-don`

**Trigger:** tích hợp xong, hủy/bỏ hướng hoặc kết thúc tài nguyên và có tài sản hay job thuộc task cần xử lý. Nhánh kết thúc ở mục 7 gọi khi cần.

1. Xác định quyết định còn hiệu lực, tài sản/job, đúng chủ, tiến trình, quyền dừng/dọn, chi phí và điều kiện phục hồi. Cửa sổ đóng hoặc PID/tên đơn lẻ không đủ làm căn cứ.
2. Ngăn ghi mới trong vùng cần chốt. Trước khi tắt, hủy hoặc dọn có thể làm mất phần dở, giữ byte chưa tích hợp, tài sản ngoài Git và chứng cứ cần lưu. Đọc lại và xác minh khả năng phục hồi bằng custody hiện có. Chưa đủ căn cứ thì giữ đúng phần bị chặn.
3. Kiểm caller, manifest/config, đường thật/symlink, runtime pointer, lịch chạy và registry liên quan. Chuyển phụ thuộc hợp lệ rồi kiểm đường chính trước khi gỡ nguồn cũ. `old/temp/untracked/ignored` không tự là rác.
4. Dừng hoặc chuyển job đúng chủ. Dịch vụ phải sống có đầu mối tiếp nhận. Dọn phần được phép, giữ quarantine byte-exact và đường phục hồi khi chính sách yêu cầu. Archive ngoài discovery, có chỉ mục và cách đọc lại. Không force-clean/reset để né quyền.
5. Xác minh tài sản, consumer và tài nguyên sau xử lý. Trả phần giữ/chuyển/dọn, job còn sống, chi phí, bằng chứng và vướng mắc cho bước đang gọi ở mục 7. Mục 8 không gọi lại workflow bàn giao, không chốt receipt hoặc nhả claim.

## 9. Triển khai một lần, sau đó giao việc bình thường

Theo trình tự chuyển đổi chung trong `CHUYEN_DOI_LUAT_VA_TIEP_TUC.md`; mục này cụ thể hóa phần skill/agent, không ban hành quy trình kích hoạt cạnh tranh.

1. Agent tại máy đọc luật cũ đang nạp và toàn cây, kiểm scope/currentness cùng hợp đồng áp dụng. Tự tìm đầu vào, không mặc định xuất gói chờ ChatGPT. Thiếu thật thì chặn đúng phần, làm phần độc lập.
2. Lập delta giữ/thay/dẫn chiếu trong task hiện có. Đối chiếu đầy đủ nghĩa vụ riêng và chỉ chuyển đúng nguồn/điều khoản được Owner giao. Khi đổi thủ tục review, đối chiếu mục 7 của quy trình chuyển luật. Giữ cổng chứng cứ, dọn dẹp, kế nhiệm và quyền phát hành.
3. Giữ byte cũ để rollback ngoài đường discovery active; thay đúng nguồn HOST/import/override/binding được giao. Không tác động luật của dự án khác hoặc để hai bản cạnh tranh; fresh-process/reopen theo host kiểm nguồn nạp và tổng giới hạn instruction chain [O10].
4. Tái dùng đường gọi phù hợp. Nếu cần native, dùng các điểm gọi `SKILL.md` có sẵn, đúng thư mục theo client/version đã xác minh. Adapter chỉ mở nguồn thao tác đã bind, không cài skill cá nhân ChatGPT thay cho repo hoặc chép lại mục 4–8 [O6].
5. Xác minh discovery và gọi thử từng trigger cần thiết; thử cả ca không nên kích hoạt, lỗi/thiếu file. Gọi skill rõ hoặc quy trình tương đương đã đọc; không coi kích hoạt ngầm chắc chắn.
6. Kiểm B/effort/fallback và quyền reviewer thực, metadata HOST, lifecycle/retention. Tái dùng gate/script/CI sẵn có, chỉ thêm kiểm xác định được đang thiếu; không dựng supervisor mới.
7. Kiểm các ca HK01–HK12 chịu ảnh hưởng trong LENH_CODEX_KIEM_TRA_SAU_THAY_LUAT.txt, trong môi trường an toàn; sửa đúng owner phần công cụ thiếu trong phạm vi. Không dùng protected data hoặc fault-inject vào production.
8. Ghi đúng mức đã đóng gói/cài/nạp/kiểm rồi dùng nhánh kết thúc ở mục 7 và tiếp phần công việc đã được giao. Không dừng sau bản kế hoạch khi việc triển khai hợp lệ còn làm được.

## 10. Nghiệm thu gọn theo rủi ro

Chọn các ca chịu ảnh hưởng ở `LENH_CODEX_KIEM_TRA_SAU_THAY_LUAT.txt` (HK01–HK12). Chứng cứ chi tiết và tình huống âm nằm tại đó. Áp cùng tiêu chí cho workflow trực tiếp và điểm gọi native đã bind. Hook/CI xanh chưa chứng minh chặn; chỉ nhận mức bảo vệ đã quan sát theo R20. Đủ chứng cứ của phần đổi thì khép kiểm và tiếp mục tiêu.

## 11. Nguồn chính thức cho adapter

Đối chiếu phiên bản và cách nạp thực tế lúc cài. AGENTS.md và nguồn riêng của dự án xác định nghĩa vụ. Tài liệu công cụ hướng dẫn adapter.

| Mã | Tài liệu |
|---|---|
| O1 | [Xem nguồn](https://learn.chatgpt.com/docs/build-skills) |
| O2 | [Xem nguồn](https://code.claude.com/docs/en/skills) |
| O3 | [Xem nguồn](https://learn.chatgpt.com/docs/agent-configuration/subagents) |
| O4 | [Xem nguồn](https://code.claude.com/docs/en/sub-agents) |
| O5 | [Xem nguồn](https://code.claude.com/docs/en/memory) |
| O6 | [Xem nguồn](https://agentskills.io/specification) |
| O7 | [Xem nguồn](https://code.claude.com/docs/en/hooks) |
| O8 | [Xem nguồn](https://learn.chatgpt.com/docs/hooks) |
| O9 | [Xem nguồn](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches) |
| O10 | [Xem nguồn](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |
